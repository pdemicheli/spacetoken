# Space Token

### Summary

Everyone complains about how siloed every blockchain application is, confined to its chosen chain and stack. Space Token breaks the barriers between blockchains by providing seamless interoperability across chains in a trustless way leveraging ZenRock's Decentralized MPC. No longer is a token confined to one chain or reliant on trusted bridges.

### How it works

Anyone who has transferred a token knows how it works. In your wallet, you switch to the chain that the token is on, select the token, enter the receiver address and amount, then hit send. Within a few seconds your tokens have been transferred to the receiver. The catch is that the receiver must be on the same chain as you.

With the Space Token standard, the transferring process is the same, except **the receiver can be on any chain** (as long as it's supported by ZenRock). When you specify the receiver address and amount, you can also select the destination chain from a dropdown before hitting send. Once again, within a few seconds your tokens have been transferred to the receiver. On the chain of your choosing. No bridge required. Powered by ZenRock.

### Use case examples

- Want to create a token for your protocol that people can trade on any chain? Make it a Space Token. It's identical to an ERC20 token on Ethereum or an SPL token on Solana (or whatever your token standard of choice is), but users can transfer it to users on different chains, and it can exist in liquidity pools on any chain.

- Want to accept SOL on your dapp on Base? Wrap it into a Space Token. Now you have SpaceSOL, that can be transferred to any chain and used like any other fungible token. You can accept SpaceSOL in your Base dapp and treat it just like SOL. If you ever need to convert it back to SOL, just transfer it back to Solana and unwrap it. No bridge needed.

- Want to use USDC on a chain where circle doesn't provide it? Use SpaceUSDC.

- Want to allow users to buy your Ethereum ERC20 token on Solana? Make it a Space Token & start a liquidity pool on Raydium.

- Need to use your NFT on Solana as collateral for a loan on Ethereum? Wrap it as a Space Token & send it where you need to on Ethereum.

### Links

- [Space Token Demo Site](https://spacetoken.aeylabs.com) - try minting some SpaceETH (`0xC7a65C034361e561083A41eC42a4f942cCb769eD` on ETH Sepolia)

- [SpaceETH Demo Video](https://drive.google.com/file/d/1dqIuZ8c5Fz3wvRrDg1phcKjotkI0IZxB)

- [GitHub Repo](https://github.com/pdemicheli/spacetoken)

### Technical details

The [demo site](https://spacetoken.aeylabs.com) allows you to interact with any Space Token smart contract as well as wrapping/unwrapping native tokens into their Space Token version. To mint your own standalone Space Tokens or wrap a native/ERC20 token into a Space Token, you can use the interactive CLI menu included in the [repo](https://github.com/pdemicheli/spacetoken), explained in `minting.md`. Currently only the native wrapping version is available in the CLI, but more experienced users can deploy their own versions of the standalone or wrapped ERC20 Space Tokens by deploying the contracts found in the repo and interacting with them directly.

Feel free to reach out to me on Telegram @pdemik with any suggestions or questions.
