import urllib.request
from collections import defaultdict

def download_and_parse_ripe_asns():
    url = 'https://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-latest'
    data = urllib.request.urlopen(url).read().decode().splitlines()
    yearly = defaultdict(int)
    for line in data:
        if line.startswith('#'):
            continue
        parts = line.split('|')
        if len(parts) < 7:
            continue
        registry, cc, t, asn, cnt, date, status = parts
        if cc == 'RU' and t == 'asn' and status == 'allocated':
            year = date[:4]
            yearly[year] += 1
    return dict(sorted(yearly.items()))
