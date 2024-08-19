// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.24;

struct AlienContract {
  address alienToken;
  bytes32 walletType;
  uint nonce;
  uint gasPrice;
  uint gas;
}

contract SpaceTokenStorage {
  address public ZR_SIGN;
  bytes32 public WALLET_TYPE;
  mapping(bytes32=>AlienContract) public alienContracts;
  mapping(bytes32=>bool) public walletTypes;
  mapping(address=>bool) public alienKeys;
  
  address public UDL; // 0x0 for SpaceAlien, 0x1 for SpaceNative, and underlying for SpaceERC.

  uint[49] __gap;
}
