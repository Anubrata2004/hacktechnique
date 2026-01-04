// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BlueCarbon {

    struct Record {
        string recordId;
        bytes32 dataHash;
        string recordType;
        uint256 timestamp;
        address verifier;
        bool exists;
    }

    mapping(bytes32 => Record) public records;

    event RecordStored(
        string recordId,
        bytes32 dataHash,
        string recordType,
        uint256 timestamp,
        address verifier
    );

    function storeRecord(
        string memory _recordId,
        bytes32 _dataHash,
        string memory _recordType
    ) public {
        require(!records[_dataHash].exists, "Record already exists");

        records[_dataHash] = Record({
            recordId: _recordId,
            dataHash: _dataHash,
            recordType: _recordType,
            timestamp: block.timestamp,
            verifier: msg.sender,
            exists: true
        });

        emit RecordStored(
            _recordId,
            _dataHash,
            _recordType,
            block.timestamp,
            msg.sender
        );
    }

    function verifyRecord(bytes32 _dataHash)
        public
        view
        returns (bool exists, string memory recordId, uint256 timestamp)
    {
        Record memory r = records[_dataHash];
        return (r.exists, r.recordId, r.timestamp);
    }
}
