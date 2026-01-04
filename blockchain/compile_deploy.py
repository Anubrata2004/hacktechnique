import json
import os
from web3 import Web3
from solcx import compile_standard, install_solc

# ---------------- CONFIG ----------------

GANACHE_URL = "http://127.0.0.1:7545"
CHAIN_ID = 1337  # Ganache default

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTRACTS_DIR = os.path.join(BASE_DIR, "../contracts")
ABI_DIR = os.path.join(BASE_DIR, "abi")

os.makedirs(ABI_DIR, exist_ok=True)

# ---------------- WEB3 SETUP ----------------

w3 = Web3(Web3.HTTPProvider(GANACHE_URL))
assert w3.is_connected(), "❌ Ganache is not running"

DEPLOYER_ADDRESS = w3.eth.accounts[0]  # AUTO SELECT FIRST GANACHE ACCOUNT

print(f"🚀 Using deployer address: {DEPLOYER_ADDRESS}")

# ---------------- SOLC SETUP ----------------

install_solc("0.8.0")

# ---------------- LOAD CONTRACTS ----------------

sources = {}
for file in os.listdir(CONTRACTS_DIR):
    if file.endswith(".sol"):
        with open(os.path.join(CONTRACTS_DIR, file), "r") as f:
            sources[file] = {"content": f.read()}

compiled = compile_standard(
    {
        "language": "Solidity",
        "sources": sources,
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "evm.bytecode"]
                }
            }
        },
    },
    solc_version="0.8.0",
)

# ---------------- DEPLOY FUNCTION ----------------

def deploy(contract_name):
    contract_data = compiled["contracts"][f"{contract_name}.sol"][contract_name]
    abi = contract_data["abi"]
    bytecode = contract_data["evm"]["bytecode"]["object"]

    # Save ABI
    with open(os.path.join(ABI_DIR, f"{contract_name}.json"), "w") as f:
        json.dump(abi, f, indent=2)

    contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    tx_hash = contract.constructor().transact({
        "from": DEPLOYER_ADDRESS
    })

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    return receipt.contractAddress

# ---------------- DEPLOY CONTRACTS ----------------

addresses = {
    "BlueCarbon": deploy("BlueCarbon"),
    "CarbonCredit": deploy("CarbonCredit")
}

# ---------------- SAVE ADDRESSES ----------------

with open(os.path.join(BASE_DIR, "contract_addresses.json"), "w") as f:
    json.dump(addresses, f, indent=2)

print("✅ Deployment successful")
print(json.dumps(addresses, indent=2))
