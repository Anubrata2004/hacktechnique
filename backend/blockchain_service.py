import json
import os
from web3 import Web3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Blockchain paths
BLOCKCHAIN_DIR = os.path.join(BASE_DIR, "../blockchain")
ABI_DIR = os.path.join(BLOCKCHAIN_DIR, "abi")

# Load contract addresses
with open(os.path.join(BLOCKCHAIN_DIR, "contract_addresses.json")) as f:
    CONTRACT_ADDRESSES = json.load(f)

# Load ABI
with open(os.path.join(ABI_DIR, "BlueCarbon.json")) as f:
    BLUE_CARBON_ABI = json.load(f)

# Web3 connection
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
assert w3.is_connected(), "Ganache not running"

DEPLOYER = w3.eth.accounts[0]

# Contract instance
blue_carbon_contract = w3.eth.contract(
    address=CONTRACT_ADDRESSES["BlueCarbon"],
    abi=BLUE_CARBON_ABI
)

def store_mrv_hash_on_chain(record_id, data_hash):
    """
    Stores MRV hash on blockchain
    """
    tx_hash = blue_carbon_contract.functions.storeRecord(
        record_id,
        bytes.fromhex(data_hash),
        "MRV"
    ).transact({"from": DEPLOYER})

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    return receipt.transactionHash.hex()
