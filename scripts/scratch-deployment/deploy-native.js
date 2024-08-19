const { ethers, upgrades } = require("hardhat");

const args = [
  "SpaceEther", // name
  "ETH", // symbol
  "0xA7AdF06a1D3a2CA827D4EddA96a1520054713E1c" // zrSign
];

async function main() {
  const Token = await ethers.getContractFactory("SpaceNative");
  const token = await upgrades.deployProxy(Token, args);
  await token.waitForDeployment();
  console.log("SpaceNative deployed to:", await token.getAddress());
}

main();
