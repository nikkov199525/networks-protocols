import sqlite3

DB_NAME = 'dnsmon.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS ip_asn (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL,
            asn TEXT,
            asn_desc TEXT,
            source TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_entry(ip, asn, asn_desc, source):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO ip_asn (ip, asn, asn_desc, source)
        VALUES (?, ?, ?, ?)
    ''', (ip, asn, asn_desc, source))
    conn.commit()
    conn.close()

def mark_as_nsdni(ip):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE ip_asn SET source = 'nsdni' WHERE ip = ?", (ip,))
    conn.commit()
    conn.close()
