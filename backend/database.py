import sqlite3
from config import Config

class Database:
    def __init__(self):
        self.db_path = Config.DATABASE_PATH
        self.init_db()

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS blockchain_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_id TEXT,
            tx_hash TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)


        cur.execute("""
        CREATE TABLE IF NOT EXISTS sites (
            site_id TEXT PRIMARY KEY,
            measurement_date TEXT,
            species TEXT,
            area_ha REAL,
            annual_sequestration REAL,
            total_carbon_stock REAL,
            mrv_status TEXT DEFAULT 'Pending',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS mrv_records (
            mrv_id TEXT PRIMARY KEY,
            site_id TEXT,
            status TEXT,
            verifier TEXT,
            verification_date TEXT,
            data_hash TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (site_id) REFERENCES sites(site_id)
        )
        """)

        conn.commit()
        conn.close()

    def insert_site(self, site):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("""
        INSERT OR REPLACE INTO sites
        (site_id, measurement_date, species, area_ha, annual_sequestration, total_carbon_stock)
        VALUES (?, ?, ?, ?, ?, ?)
        """, site)
        conn.commit()
        conn.close()

    def get_sites(self):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM sites")
        rows = cur.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def update_mrv_status(self, site_id, status):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("""
        UPDATE sites SET mrv_status = ? WHERE site_id = ?
        """, (status, site_id))
        conn.commit()
        conn.close()
def insert_blockchain_log(self, site_id, tx_hash):
    conn = self.connect()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO blockchain_logs (site_id, tx_hash)
    VALUES (?, ?)
    """, (site_id, tx_hash))
    conn.commit()
    conn.close()
