import sqlite3
from datetime import datetime

DB_FILE = "visitors.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS visitor_log (
            ip TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_ip(ip):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO visitor_log (ip, timestamp) VALUES (?, ?)", (ip, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def get_logs():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM visitor_log ORDER BY timestamp DESC")
    logs = c.fetchall()
    conn.close()
    return logs
