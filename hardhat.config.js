require("@nomicfoundation/hardhat-toolbox");
require("@openzeppelin/hardhat-upgrades");

require("dotenv").config();

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    version: "0.8.24",
    settings: {
      optimizer: {
        enabled: true,
        runs: 1
      }
    }
  },
  networks: {
    amoy: {
      url: process.env.POLYGON_AMOY_ENDPOINT,
      accounts: [process.env.PK]
    },
    sepolia: {
      url: process.env.ETHEREUM_SEPOLIA_ENDPOINT,
      accounts: [process.env.PK]
    },
    baseSepolia: {
      url: process.env.BASE_SEPOLIA_ENDPOINT,
      accounts: [process.env.PK]
    },
  },
  etherscan: {
    apiKey: {
      sepolia: process.env.ETHERSCAN_API,
      polygonAmoy: process.env.POLYGONSCAN_API,
      baseSepolia: process.env.BASESCAN_API,
    }
  },
  sourcify: {
    enabled: true
  }
};
