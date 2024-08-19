// Required environment args: TARGET, CHAIN_ID, WALLET_TYPE, ALIEN_TOKEN, NONCE, GAS_PRICE, GAS, KEY

const { ethers } = require("hardhat");

async function main() {
  const args = [
    process.env.TARGET,
    process.env.CHAIN_ID,
    process.env.WALLET_TYPE,
    process.env.ALIEN_TOKEN,
    process.env.NONCE,
    process.env.GAS_PRICE,
    process.env.GAS,
    process.env.KEY
  ]
  if (args.includes(undefined)) throw new Error("Missing args.");

  const token = await ethers.getContractAt("SpaceToken", process.env.TARGET);
  const tx = await token.registerAlien(...(args.slice(1)));
  await tx.wait();
}

main();
