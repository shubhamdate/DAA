pragma solidity 0.4.25;

contract Bank{
    uint Bal;
    constructor() public{
        Bal = 1;
    }
    function depositMoney(uint amt ) public{
        Bal+=amt;
    }
    function withdrawMoney(uint amt) public{
        Bal-=amt;
    }
    function showBalance() view public returns(uint){
        return Bal; 
    } 
}