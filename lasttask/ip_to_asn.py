import socket
from ipwhois import IPWhois

def radb_lookup(ip: str) -> str | None:
    try:
        with socket.create_connection(("whois.radb.net", 43), 3) as s:
            s.sendall((ip + "\r\n").encode())
            data = s.recv(8192).decode(errors="ignore")
        for line in data.splitlines():
            if line.lower().startswith("origin:"):
                return line.split()[-1]
    except Exception:
        pass
    return None

def get_as_info(ip: str):
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        asn = res.get("asn")
        desc = res.get("asn_description", "N/A")
    except Exception:
        asn = None
        desc = "N/A"

    if asn in (None, 'NA', '0'):
        alt = radb_lookup(ip)
        if alt:
            asn = alt
            desc = "via RADB"

    return {"ip": ip, "asn": asn, "asn_desc": desc}