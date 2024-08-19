// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.24;

import { ERC20 } from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import { SpaceToken } from "./SpaceToken.sol";

contract SpaceERC is SpaceToken {
  function initialize(
    address underlying,
    address zrSign
  ) public initializer {
    ZR_SIGN = zrSign;
    UDL = underlying;
    ERC20 udlContract = ERC20(underlying);
    __ERC20_init(udlContract.name(), udlContract.symbol());
    __Ownable_init(msg.sender);
  }

  function deposit(uint value) external {
    ERC20(UDL).transferFrom(msg.sender, address(this), value);
    _mint(msg.sender, value);
  }

  function withdraw(uint value) external {
    _burn(msg.sender, value);
    ERC20(UDL).transfer(msg.sender, value);
  }
}
