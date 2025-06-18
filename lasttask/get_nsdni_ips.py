import socket

NSDNI_HOSTS = [
    'dns1.nsdninet.ru',
    'dns2.nsdninet.ru',
    'dns3.nsdninet.ru',
    'dns4.nsdninet.ru'
]

def resolve_nsdni_hosts():
    ips = set()
    for h in NSDNI_HOSTS:
        try:
            _, _, addrs = socket.gethostbyname_ex(h)
            ips.update(addrs)
        except Exception:
            pass
    return list(ips)
