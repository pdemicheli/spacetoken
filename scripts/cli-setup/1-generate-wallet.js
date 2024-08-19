// Required environment args: TARGET, WALLET_TYPE

const { ethers } = require("hardhat");

async function main() {
  const args = [
    process.env.TARGET,
    process.env.WALLET_TYPE
  ]
  if (args.includes(undefined)) throw new Error("Missing args.");

  const token = await ethers.getContractAt("SpaceToken", process.env.TARGET);
  const ZR_SIGN = await token.ZR_SIGN();
  const zrSign = await ethers.getContractAt("IZrSign", ZR_SIGN);
  let keys = await zrSign.getZrKeys(process.env.WALLET_TYPE, process.env.TARGET);
  if (keys.length != 0) throw new Error("Shouldn't create more than one wallet.");
  
  // const fees = await zrSign["estimateFee(uint8, uint256)"](1, 0); // Not working for base fee, recalculate manually
  const block = await ethers.provider.getBlock("latest");
  const mpcFee = await zrSign.getMPCFee();
  const netRespFee = (await zrSign.getRespGas()) * (block.baseFeePerGas * (await zrSign.getRespGasPriceBuffer())/100n);
  const totalFee = mpcFee + netRespFee;

  const tx = await token.createWallet(process.env.WALLET_TYPE, { value: totalFee*12n/10n }); // *1.2 for good measure
  await tx.wait();

  // Wait for Res transaction and grab key
  while (keys.length == 0) {
    keys = await zrSign.getZrKeys(process.env.WALLET_TYPE, process.env.TARGET);
    await new Promise(r => setTimeout(r, 500));
  }
  
  console.log(keys[0]);
}

main();
