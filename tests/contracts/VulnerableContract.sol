pragma solidity ^0.4.24;

contract VulnerableContract {
    mapping(address => uint) public balances;

    function withdraw() public {
        if (msg.sender.call.value(balances[msg.sender])()) {
            balances[msg.sender] = 0;
        }
    }

    function authenticate() public view returns (bool) {
        return tx.origin == msg.sender;
    }

    function sendEther(address recipient) public {
        recipient.transfer(1 ether);
    }
}
