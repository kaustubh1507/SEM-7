// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }

    mapping(uint => Candidate) public candidates;
    mapping(address => bool) public voters;

    uint public candidatesCount;
    uint public totalVotes;

    event Voted(address indexed voter, uint indexed candidateId);

    constructor(string[] memory candidateNames) {
        for (uint i = 0; i < candidateNames.length; i++) {
            addCandidate(candidateNames[i]);
        }
    }

    function addCandidate(string memory name) private {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, name, 0);
    }

    function vote(uint candidateId) public {
        require(!voters[msg.sender], "You have already voted.");
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID.");

        voters[msg.sender] = true;
        candidates[candidateId].voteCount++;
        totalVotes++;

        emit Voted(msg.sender, candidateId);
    }

    function getCandidate(uint candidateId) public view returns (Candidate memory) {
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID.");
        return candidates[candidateId];
    }

    function getResults() public view returns (uint[] memory candidateIds, uint[] memory voteCounts) {
        candidateIds = new uint[](candidatesCount);
        voteCounts = new uint[](candidatesCount);

        for (uint i = 1; i <= candidatesCount; i++) {
            candidateIds[i - 1] = candidates[i].id;
            voteCounts[i - 1] = candidates[i].voteCount;
        }
    }
}
