// Required environment args: KEY

const { ethers } = require("hardhat");

async function main() {
  if (process.env.KEY == undefined) throw new Error("Missing arg.");

  const [signer] = await ethers.getSigners();
  const tx = await signer.sendTransaction({to: process.env.KEY, value: ethers.parseEther("0.01")});
  await tx.wait();
}

main();
