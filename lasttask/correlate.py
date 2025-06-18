import sqlite3
from datetime import datetime, timedelta

DB_NAME = 'dnsmon.db'
WINDOW_MIN = 5

def find_correlated_events():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT ip, timestamp FROM ip_asn WHERE source='dns'")
    dns_rows = c.fetchall()
    correlated = []
    for ip, ts in dns_rows:
        dns_time = datetime.fromisoformat(ts)
        start = dns_time - timedelta(minutes=WINDOW_MIN)
        end = dns_time + timedelta(minutes=WINDOW_MIN)
        c.execute("""SELECT source, timestamp FROM ip_asn
                      WHERE ip=? AND source IN ('http','js')
                      AND timestamp BETWEEN ? AND ?""", (ip, start.isoformat(), end.isoformat()))
        for src, t2 in c.fetchall():
            correlated.append({'ip': ip, 'dns_time': ts, 'event_time': t2, 'source': src})
    conn.close()
    return correlated
