import re

def parse_dns_log(file_path):
    pat = re.compile(r'client @\S+ (\d+\.\d+\.\d+\.\d+)#')
    ips = set()
    try:
        with open(file_path, 'r') as f:
            for line in f:
                m = pat.search(line)
                if m:
                    ip = m.group(1)
                    if not ip.startswith(('10.', '192.168.', '127.')):
                        ips.add(ip)
    except FileNotFoundError:
        pass
    return list(ips)
