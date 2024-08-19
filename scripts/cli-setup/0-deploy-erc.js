// Required environment args: NAME, SYMBOL, ZR_SIGN

const { ethers, upgrades } = require("hardhat");

async function main() {
  const args = [
    process.env.UNDERLYING,
    process.env.ZR_SIGN
  ]
  if (args.includes(undefined)) throw new Error("Missing args.");

  const Token = await ethers.getContractFactory("SpaceERC");
  const token = await upgrades.deployProxy(Token, args);
  await token.waitForDeployment();
  console.log(await token.getAddress());
}

main();
