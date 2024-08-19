// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.24;

import { SpaceToken } from "./SpaceToken.sol";
import { ReentrancyGuardUpgradeable } from "@openzeppelin/contracts-upgradeable/utils/ReentrancyGuardUpgradeable.sol";

/** @dev SpaceToken that can be deposited/withdrawn and its underlying token is the gas token of its chain. */
contract SpaceNative is SpaceToken, ReentrancyGuardUpgradeable {
  function initialize(
    string memory name,
    string memory symbol,
    address zrSign
  ) public initializer {
    ZR_SIGN = zrSign;
    UDL = address(1);
    __ERC20_init(name, symbol);
    __Ownable_init(msg.sender);
    __ReentrancyGuard_init();
  }
  
  function deposit() external payable {
    _mint(msg.sender, msg.value);
  }

  function withdraw(uint value) external nonReentrant {
    _burn(msg.sender, value);
    payable(msg.sender).transfer(value);
  }
}
