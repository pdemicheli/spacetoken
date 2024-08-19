// Checks for balance of at least 1 to cover deploying, funding, transacting

const { ethers } = require("hardhat");

async function main() {
  const [signer] = await ethers.getSigners();
  const balance = await ethers.provider.getBalance(signer.address);
  console.log(balance);
}

main();
