// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.24;

import { SpaceToken } from "./SpaceToken.sol";

contract SpaceAlien is SpaceToken {
  function initialize(
    string memory name,
    string memory symbol,
    address zrSign
  ) public virtual initializer {
    ZR_SIGN = zrSign;
    UDL = address(0);
    __ERC20_init(name, symbol);
    __Ownable_init(msg.sender);
  }
}
