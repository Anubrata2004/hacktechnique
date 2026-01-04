from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime
from blockchain_service import store_mrv_hash_on_chain

from config import Config
from database import Database
from data_processor import DataProcessor

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db = Database()
processor = DataProcessor()

os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

@app.route("/api/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file"}), 400

    file = request.files["file"]
    if not file.filename.endswith(".csv"):
        return jsonify({"error": "Only CSV allowed"}), 400

    path = os.path.join(Config.UPLOAD_FOLDER, file.filename)
    file.save(path)

    df = processor.load_csv(path)
    df = processor.clean(df)
    sites = processor.process_sites(df)

    for site in sites:
        db.insert_site(site)

    return jsonify({
        "message": "Dataset processed",
        "sites_added": len(sites)
    })

@app.route("/api/sites", methods=["GET"])
def get_sites():
    return jsonify(db.get_sites())

@app.route("/api/verify/<site_id>", methods=["POST"])
def verify_site(site_id):
    # Mark MRV as verified
    db.update_mrv_status(site_id, "Verified")

    # Generate hash for blockchain
    sites = db.get_sites()
    site = next(s for s in sites if s["site_id"] == site_id)

    raw_data = f"{site['site_id']}{site['area_ha']}{site['annual_sequestration']}"
    import hashlib
    data_hash = hashlib.sha256(raw_data.encode()).hexdigest()

    # Store on blockchain
    tx_hash = store_mrv_hash_on_chain(site_id, data_hash)

    # Store tx hash in DB
    db.insert_blockchain_log(site_id, tx_hash)

    return jsonify({
        "site_id": site_id,
        "status": "Verified",
        "blockchain_tx": tx_hash
    })


if __name__ == "__main__":
    app.run(debug=True)
