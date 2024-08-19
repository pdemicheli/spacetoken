// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.24;

import { SpaceTokenStorage, AlienContract } from "./storage/SpaceTokenStorage.sol";
import { ERC20Upgradeable } from "@openzeppelin/contracts-upgradeable/token/ERC20/ERC20Upgradeable.sol";
import { OwnableUpgradeable } from "@openzeppelin/contracts-upgradeable/access/OwnableUpgradeable.sol";
import { IZrSign } from "./interfaces/IZrSign.sol";
import { SignTypes } from "./libraries/SignTypes.sol";
import { Lib_RLPWriter } from "./libraries/Lib_RLPWriter.sol";

error WalletTypeCreated();
error WalletTypeNotCreated();
error AddressNotAuthorized();
error ChainNotRegistered();

/** @dev SpaceToken that cannot be deposited/withdrawn. */
abstract contract SpaceToken is SpaceTokenStorage, ERC20Upgradeable, OwnableUpgradeable {
  using Lib_RLPWriter for uint;
  using Lib_RLPWriter for address;
  using Lib_RLPWriter for bytes;
  using Lib_RLPWriter for bytes[];

  /// @custom:oz-upgrades-unsafe-allow constructor
  constructor() {
    _disableInitializers();
  }

  function createWallet(bytes32 walletType) external payable {
    if (walletTypes[walletType]) revert WalletTypeCreated();
    IZrSign(ZR_SIGN).zrKeyReq{ value: msg.value }(SignTypes.ZrKeyReqParams({
      walletTypeId: walletType,
      options: 1
    }));
    walletTypes[walletType] = true;
  }

  /** @dev Used in outbound transfers. Nonce should almost always be 0. Ethereum gas price 50e9 and gas 210000. */
  function registerAlienContract(
    bytes32 chainId,
    bytes32 walletType,
    address alienToken,
    uint nonce,
    uint gasPrice,
    uint gas
  ) public onlyOwner {
    if (!walletTypes[walletType]) revert WalletTypeNotCreated();
    alienContracts[chainId] = AlienContract(alienToken, walletType, nonce, gasPrice, gas);
  }

  /** @dev Used in inbound transfers. */
  function registerAlienKey(address key, bool status) public onlyOwner {
    alienKeys[key] = status;
  }

  /** @dev Helper to setup inbound & outbound transfers together. */
  function registerAlien(
    bytes32 chainId,
    bytes32 walletType,
    address alienToken,
    uint nonce,
    uint gasPrice,
    uint gas,
    address key
  ) external onlyOwner {
    registerAlienContract(chainId, walletType, alienToken, nonce, gasPrice, gas);
    registerAlienKey(key, true);
  }

  function mint(address account, uint value) external {
    // Ensure sender is registered alien (inbound transfer)
    if (!alienKeys[msg.sender]) revert AddressNotAuthorized();
    _mint(account, value);
  }

  function spaceTransfer(address to, uint value, bytes32 chainId) external payable {
    AlienContract memory alien = alienContracts[chainId];
    if (alien.alienToken == address(0)) revert ChainNotRegistered();

    // Burn tokens

    _burn(msg.sender, value);

    // Encode transaction data

    bytes memory method = abi.encodeWithSignature("mint(address,uint256)", to, value);

    bytes memory rlpZero = uint(0).writeUint();

    bytes[] memory transaction = new bytes[](9);
    transaction[0] = alien.nonce.writeUint(); // nonce      
    transaction[1] = alien.gasPrice.writeUint(); // gas price
    transaction[2] = alien.gas.writeUint(); // gas
    transaction[3] = alien.alienToken.writeAddress(); // to
    transaction[4] = rlpZero; // value
    transaction[5] = method.writeBytes(); // data
    transaction[6] = rlpZero;
    transaction[7] = rlpZero;
    transaction[8] = rlpZero;

    bytes memory data = transaction.writeList();

    // Send to zrSign

    IZrSign(ZR_SIGN).zrSignTx{ value: msg.value }(SignTypes.ZrSignParams({
      walletTypeId: alien.walletType,
      walletIndex: 0,
      dstChainId: chainId,
      payload: data,
      broadcast: true
    }));

    alienContracts[chainId].nonce++;
  }

  /** @dev Need receive function for fee rebate. */
  receive() external payable {}

  /** @dev Temporary. */
  function drain() external onlyOwner {
    payable(msg.sender).transfer(address(this).balance);
  }

  function setNonce(bytes32 chainId, uint nonce) external onlyOwner {
    alienContracts[chainId].nonce = nonce;
  }

  function setUDL(address udl) external onlyOwner {
    UDL = udl;
  }

  // function spaceApprove(address spender, uint value, bytes32 chain) external {}

  // function spaceTransferFrom(address from, address to, uint value, bytes32 chain) external {}
}
