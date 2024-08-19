const { ethers, upgrades } = require("hardhat");

const tokenAddress = "0xbd4c9fC10c099DfCeB17f866aeA1e9015C0a87F0";

async function main() {
  const Token = await ethers.getContractFactory("SpaceNative");
  await upgrades.upgradeProxy(tokenAddress, Token);
  console.log("SpaceNative upgraded");
}

main();