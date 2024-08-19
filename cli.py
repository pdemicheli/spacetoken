#!/usr/bin/env python3

from simple_term_menu import TerminalMenu
from subprocess import check_output
import os
import json
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

# Override TerminalMenu so Q or escape aborts
class TerminalMenu(TerminalMenu):
  def show(self):
    result = super().show()
    if result == None:
      abort()
    return result
def abort(*_):
  print("Aborted.")
  os._exit(0)
def run(cmd):
  # return input(f"For now run and paste input: {cmd} | ")
  return check_output(cmd, shell=True, text=True).strip()

DEPLOYMENTS = "cli-deployments.json"

class WalletTypes:
  EVM = "0xe146c2986893c43af5ff396310220be92058fb9f4ce76b929b80ef0d5307100a"

class Chains:
  # SpaceNative-compatible chains need name and symbol
  # Chain IDs: keccak256("eip155:<chain_id>")
  EthereumSepolia = {
    "network": "sepolia",
    "zr_sign": "0xA7AdF06a1D3a2CA827D4EddA96a1520054713E1c",
    "chain_id": "0xafa90c317deacd3d68f330a30f96e4fa7736e35e8d1426b2e1b2c04bce1c2fb7",
    "wallet_type": WalletTypes.EVM,
    "gas_price": 50000000000,
    "gas": 210000,
    "name": "Ether",
    "symbol": "ETH",
    "api": "ETHEREUM_SEPOLIA_ENDPOINT"
  }
  PolygonAmoy = {
    "network": "amoy",
    "zr_sign": "0xA7AdF06a1D3a2CA827D4EddA96a1520054713E1c",
    "chain_id": "0x4df3b2a1df4e086e001def1ba6466078aa6aaf12e7a183f590364b811b18ee5b",
    "wallet_type": WalletTypes.EVM,
    "gas_price": 50000000000,
    "gas": 210000,
    "name": "Matic",
    "symbol": "MATIC",
    "api": "POLYGON_AMOY_ENDPOINT"
  }
  AvalancheFuji = {
    "network": "fuji", # check
    "zr_sign": "0xA7AdF06a1D3a2CA827D4EddA96a1520054713E1c",
    "chain_id": "0x5f3f93115d7efd19d933ee81a3fe76ec1e0f35d41927d6fe0875a4f4c29345da",
    "wallet_type": WalletTypes.EVM,
    "gas_price": 50000000000, # check
    "gas": 210000, # check
    "name": "Avalanche",
    "symbol": "AVAX",
    "api": "AVALANCHE_FUJI_ENDPOINT"
  }
  BinanceTestnet = {
    "network": "binanceTestnet", # check
    "zr_sign": "0xA7AdF06a1D3a2CA827D4EddA96a1520054713E1c",
    "chain_id": "0x42a13880db2f2fe1c95fc8d04876a774745355a97dfe8f3397694d11f135eccf",
    "wallet_type": WalletTypes.EVM,
    "gas_price": 50000000000, # check
    "gas": 210000, # check
    "name": "Binance Coin",
    "symbol": "BNB",
    "api": "BINANCE_TESTNET_ENDPOINT"
  }
  ArbitrumSepolia = {
    "network": "arbitrumSepolia", # check
    "zr_sign": "0xA7AdF06a1D3a2CA827D4EddA96a1520054713E1c",
    "chain_id": "0xf0b5e5225193cfd0cd1b399b5597eb35e33f77deb76267030dc6d28cf2a8d16b",
    "wallet_type": WalletTypes.EVM,
    "gas_price": 50000000000, # check
    "gas": 210000, # check
    "api": "ARBITRUM_SEPOLIA_ENDPOINT"
  }
  OptimismSepolia = {
    "network": "optimismSepolia", # check
    "zr_sign": "0xA7AdF06a1D3a2CA827D4EddA96a1520054713E1c",
    "chain_id": "0xed0d19ae6067b72db99bcb0dc8751b7d9a0733d390cef703366aa5c2ab3cc467",
    "wallet_type": WalletTypes.EVM,
    "gas_price": 50000000000, # check
    "gas": 210000, # check
    "api": "OPTIMISM_SEPOLIA_ENDPOINT"
  }
  BaseSepolia = {
    "network": "baseSepolia",
    "zr_sign": "0xA7AdF06a1D3a2CA827D4EddA96a1520054713E1c",
    "chain_id": "0x8a9a9c58b754a98f1ff302a7ead652cfd23eb36a5791767b5d185067dd9481c2",
    "wallet_type": WalletTypes.EVM,
    "gas_price": 50000000000, # check
    "gas": 210000, # check
    "api": "BASE_SEPOLIA_ENDPOINT"
  }

def environmentChecks(chain1, chain2):
  # Add .env checks (private keys, rpc api keys)
  for x in ["PK", chain1["api"], chain2["api"]]:
    assert x in os.environ, "Missing environment variable."
def balanceChecks(chain1, chain2):
  # Add balance checks (for deploying, transacting, funding)
  bal1 = run(f"npx hardhat run scripts/cli-setup/get-balance.js --network {chain1['network']}")
  bal1 = bal1 if bal1.isdigit() else bal1[:-1]
  assert int(bal1)/1e18 > 0.04, f"Need balance of at least 0.04 on {chain1['network']}."
  bal2 = run(f"npx hardhat run scripts/cli-setup/get-balance.js --network {chain2['network']}")
  bal2 = bal2 if bal2.isdigit() else bal2[:-1]
  assert int(bal2)/1e18 > 0.04, f"Need balance of at least 0.04 on {chain2['network']}."

def spaceERCMenu():
  print("Work in progress.")
  abort()
def spaceAlienMenu():
  print("Work in progress.")
  abort()

def spaceNativeSetup(native_chain, alien_chain):
  token_name = "Space " + native_chain["name"]
  token_symbol = "Space" + native_chain["symbol"]
  # 1. Native chain setup
  # 1.1. Deploy native contract
  print("Deploying native contract.")
  native_address = run(
    f"NAME='{token_name}' SYMBOL='{token_symbol}' "
    "ZR_SIGN={zr_sign} npx hardhat run scripts/cli-setup/0-deploy-native.js --network {network}"
    .format(**native_chain)
  )
  # 1.2. Generate native key
  print("Generating native key.")
  native_key = run(
    "TARGET={target_contract} WALLET_TYPE={wallet_type} "
    "npx hardhat run scripts/cli-setup/1-generate-wallet.js --network {network}"
    .format(target_contract=native_address, **native_chain)
  )
  # 1.3. Fund native key on alien network
  print("Funding native key on alien network.")
  run(f"KEY={native_key} npx hardhat run scripts/cli-setup/2-fund-wallet.js --network {alien_chain['network']}")

  # 2. Alien chain setup
  # 2.1. Deploy alien contract
  print("Deploying alien contract.")
  alien_address = run(
    f"NAME='{token_name}' SYMBOL='{token_symbol}' "
    "ZR_SIGN={zr_sign} npx hardhat run scripts/cli-setup/0-deploy-alien.js --network {network}"
    .format(**alien_chain)
  )
  # 2.2. Generate alien key
  print("Generating alien key.")
  alien_key = run(
    "TARGET={target_contract} WALLET_TYPE={wallet_type} "
    "npx hardhat run scripts/cli-setup/1-generate-wallet.js --network {network}"
    .format(target_contract=alien_address, **alien_chain)
  )
  # 2.3. Fund alien key on native neywork
  print("Funding alien key on native network.")
  run(f"KEY={alien_key} npx hardhat run scripts/cli-setup/2-fund-wallet.js --network {native_chain['network']}")

  # 3. Link
  # 3.1. Register alien key and contract on native contract
  print("Registering alien key and contract on native contract.")
  run(
    "TARGET={target_contract} CHAIN_ID={chain_id} WALLET_TYPE={wallet_type} "
    "ALIEN_TOKEN={alien_token} NONCE={nonce} GAS_PRICE={gas_price} GAS={gas} KEY={key} "
    "npx hardhat run scripts/cli-setup/3-register-alien.js --network {target_network}"
    .format(
      target_contract=native_address,
      alien_token=alien_address,
      nonce="0",
      key=alien_key,
      target_network=native_chain["network"],
      **alien_chain # chain_id, wallet_type, gas_price, gas
    )
  )
  # 3.2. Register native key and contract on alien contract
  print("Registering native key and contract on alien contract.")
  run(
    "TARGET={target_contract} CHAIN_ID={chain_id} WALLET_TYPE={wallet_type} "
    "ALIEN_TOKEN={alien_token} NONCE={nonce} GAS_PRICE={gas_price} GAS={gas} KEY={key} "
    "npx hardhat run scripts/cli-setup/3-register-alien.js --network {target_network}"
    .format(
      target_contract=alien_address,
      alien_token=native_address,
      nonce="0",
      key=native_key,
      target_network=alien_chain["network"],
      **native_chain # chain_id, wallet_type, gas_price, gas
    )
  )

  dep = {
    "native": {
      "network": native_chain["network"],
      "contract": native_address,
      "key": native_key
    },
    "aliens": [
      {
      "network": alien_chain["network"],
      "contract": alien_address,
      "key": alien_key
      }
    ]
  }

  print()
  print("Saving deployment:")
  pprint(dep)
  
  print()
  print("Verify contracts with:")
  print(f"- npx hardhat verify {native_address} --network {native_chain['network']}")
  print(f"- npx hardhat verify {alien_address} --network {alien_chain['network']}")

  return dep

def spaceNativeMenu():
  native_chain = [
    Chains.EthereumSepolia,
    Chains.PolygonAmoy,
    Chains.AvalancheFuji,
    Chains.BinanceTestnet
  ][TerminalMenu([
    "[1] Ethereum Sepolia (ETH)",
    "[2] Polygon Amoy (MATIC)",
    "[3] Avalanche Fuji (AVAX)",
    "[4] Binance Testnet (BNB)"
  ], title="Select Native Token Chain:").show()]

  alien_chain = [
    Chains.EthereumSepolia,
    Chains.PolygonAmoy,
    Chains.AvalancheFuji,
    Chains.BinanceTestnet,
    Chains.ArbitrumSepolia,
    Chains.OptimismSepolia,
    Chains.BaseSepolia,
  ][TerminalMenu([
    "[1] Ethereum Sepolia",
    "[2] Polygon Amoy",
    "[3] Avalanche Fuji",
    "[4] Binance Testnet",
    "[5] Arbitrum Sepolia",
    "[6] Optimism Sepolia",
    "[7] Base Sepolia"
  ], title="Select Alien Token Chain:").show()]

  if native_chain == alien_chain:
    print("Native and Alien chains must differ.")
    return spaceNativeMenu()
  
  print("""Executing the following steps:
  1. Deploy SpaceToken Contracts
  2. Generate Wallets
  3. Fund Wallets
  4. Register Keys (to allow inbound transfers)
  5. Register Contracts (to allow outbound transfers)""")

  print("Compiling and checking for sufficient balance.")
  run("npx hardhat compile")
  environmentChecks(native_chain, alien_chain)
  balanceChecks(native_chain, alien_chain)

  # Result is deployment info, write to file
  result = [
    spaceNativeSetup,
    abort,
  ][TerminalMenu([
    "[y] Continue",
    "[n] Abort",
  ], title="Continue?").show()](native_chain, alien_chain)

  with open(DEPLOYMENTS, "r") as f:
    deps = json.load(f)
  deps["SpaceNative"] = deps.get("SpaceNative", []) + [result]
  with open(DEPLOYMENTS, "w") as f:
    json.dump(deps, f, indent=2)

def main():
  print("SpaceToken Interactive Menu. Press Q to abort.")
  [
    spaceNativeMenu,
    spaceERCMenu,
    spaceAlienMenu
  ][TerminalMenu([
    "[1] Create SpaceNative Token (+ first SpaceAlien)",
    "[2] Create SpaceERC Token (+ first SpaceAlien)",
    "[3] Create SpaceAlien Token (for existing SpaceToken)"
  ], title="Select Action:").show()]()

if __name__ == "__main__":
  main()

# Can add multi-select for "which chains do you want to deploy an alien contract on?":
# https://pypi.org/project/simple-term-menu/#:~:text=Multi%2Dselect%20example
