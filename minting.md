# Space Token Deployment Checklist

This checklist is covered by the interactive command-line menu `cli.py` (install required pip libraries). That should be used to deploy Space Tokens. This checklist covers what must be done in order to deploy a Space Token manually. Before starting, populate a `.env` file with the fields included in `.env.example` and add/remove networks in `hardhat.config.js` as needed.

1. **Deploy Contracts (SpaceNative.sol, SpaceERC.sol, SpaceAlien.sol)**
- ZrSign Contract on most chains: `0xA7AdF06a1D3a2CA827D4EddA96a1520054713E1c`.

2. **Generate Keys on both chains**
- Call `createWallet()`.

3. **Fund Keys on both chains**
- Transfer the gas token on both chains to the first contract's generated key on the second chain and the second contract's generated key on the first chain.

4. **Register Keys & Contracts (allow inbound & outbound transfers respectively)**
- Call `registerAlien()` on both contracts.

5. **Space Transfer**
- Use `spaceTransfer()`.

I plan on building a contract which executes this all automatically, deploying the Space Token contract on foreign chains automatically using deployment transactions signed through ZrSign and broadcasted by the ZenRock chain in order to largely simplify the deployment process.

Feel free to reach out to me on Telegram @pdemik with any suggestions or if you need further clarification.
