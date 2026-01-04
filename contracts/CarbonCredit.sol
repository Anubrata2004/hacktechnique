// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CarbonCredit {

    struct Credit {
        string creditId;
        uint256 amount;
        address owner;
        bool retired;
    }

    mapping(string => Credit) public credits;
    mapping(address => uint256) public balances;

    address public admin;

    event CreditMinted(string creditId, address owner, uint256 amount);
    event CreditTransferred(string creditId, address from, address to);
    event CreditRetired(string creditId, address owner);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin allowed");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    function mintCredit(
        string memory _creditId,
        address _to,
        uint256 _amount
    ) public onlyAdmin {
        require(_amount > 0, "Invalid amount");
        require(!credits[_creditId].retired, "Credit exists");

        credits[_creditId] = Credit({
            creditId: _creditId,
            amount: _amount,
            owner: _to,
            retired: false
        });

        balances[_to] += _amount;

        emit CreditMinted(_creditId, _to, _amount);
    }

    function transferCredit(string memory _creditId, address _to) public {
        Credit storage c = credits[_creditId];
        require(c.owner == msg.sender, "Not owner");
        require(!c.retired, "Credit retired");

        balances[msg.sender] -= c.amount;
        balances[_to] += c.amount;
        c.owner = _to;

        emit CreditTransferred(_creditId, msg.sender, _to);
    }

    function retireCredit(string memory _creditId) public {
        Credit storage c = credits[_creditId];
        require(c.owner == msg.sender, "Not owner");
        require(!c.retired, "Already retired");

        c.retired = true;
        balances[msg.sender] -= c.amount;

        emit CreditRetired(_creditId, msg.sender);
    }
}
