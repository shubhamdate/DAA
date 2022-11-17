pragma solidity 0.8.0;

contract studentData{
    struct student{
        int rollNo;
        string name;
    }

    student[] record;
    function addStudentData(int rollNo, string memory name) public {
        record.push(student(rollNo, name));

    }
    function showrecord() public view returns(student[] memory){
        return record;
    } 
    fallback() external payable{
        delete record;
    }
}