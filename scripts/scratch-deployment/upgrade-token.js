const { ethers, upgrades } = require("hardhat");

const tokenAddress = "";

async function main() {
  const Token = await ethers.getContractFactory("SpaceNative");
  await upgrades.upgradeProxy(tokenAddress, Token);
  console.log("SpaceNative upgraded");
}

main();