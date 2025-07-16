import sqlite3
from datetime import datetime

conn = sqlite3.connect("ip_log.db", check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ip_log (
            local_ip TEXT,
            public_ip TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()

def log_ip(local_ip, public_ip):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO ip_log (local_ip, public_ip, timestamp) VALUES (?, ?, ?)",
        (local_ip, public_ip, timestamp)
    )
    conn.commit()

def get_logs():
    cursor.execute("SELECT * FROM ip_log ORDER BY timestamp DESC")
    return cursor.fetchall()
