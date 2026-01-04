Blockchain-Based Blue Carbon MRV System
📌 What is this project?

This project is a full-stack Blockchain-based Monitoring, Reporting, and Verification (MRV) system for Blue Carbon ecosystems such as mangroves, seagrass, and coastal wetlands.
It enables transparent collection, verification, and immutable storage of restoration and plantation data, and supports carbon credit generation from verified blue carbon projects.

The system integrates:

Field data ingestion (CSV-based MRV datasets)

Backend processing and verification

Blockchain anchoring for tamper-proof records

A web-based user interface for interaction and visualization

🌍 Why is this project important?

Blue carbon ecosystems play a critical role in climate change mitigation by sequestering large amounts of carbon.
However, existing MRV systems often suffer from:

Centralized data storage

Lack of transparency

Difficulty in verification

Risk of data manipulation

This project addresses these issues by:

Ensuring data immutability using blockchain

Providing traceable verification workflows

Enabling trustworthy carbon credit generation

Supporting NGOs, communities, and governing bodies with a transparent MRV platform

It aligns with India’s climate goals and global carbon market standards.

🧰 Technology Stack
🔹 Frontend

ReactJS

HTML, CSS

REST API integration

🔹 Backend

Python (Flask)

SQLite3 (lightweight relational database)

Pandas (data processing)

🔹 Blockchain

Solidity (Smart Contracts)

Ganache (Local Ethereum network)

Web3.py (Python–Blockchain interaction)

solcx (py-solc-x) for contract compilation

🔹 Tools

Git & GitHub

VS Code

Postman (API testing)

⚙️ Project Workflow

MRV datasets are uploaded via the web interface

Backend processes and stores data in SQLite

Admin verification triggers MRV validation

Verified MRV data is hashed and stored on blockchain

Blockchain transaction hash is recorded for auditability

Carbon credits are derived from verified MRV data

Users can view records, verification status, and credits via UI

✅ Current Project Status

✔ Backend API fully implemented
✔ MRV data ingestion and processing completed
✔ SQLite database integrated
✔ Smart contracts written and deployed
✔ Blockchain integration completed using Python
✔ ABI and contract addresses generated automatically
✔ Frontend UI implemented (Dashboard, Upload, Records, Verify, Credits)
✔ End-to-end demo flow working




How to Run the Project

Start Ganache (Quickstart Ethereum)

Run backend:

cd backend
python app.py


Run frontend:

cd frontend
npm install
npm start


Access UI at:

http://localhost:3000
