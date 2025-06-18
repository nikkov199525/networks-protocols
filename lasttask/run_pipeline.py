from parse_http_logs import parse_access_log
from parse_dns_logs import parse_dns_log
from ip_to_asn import get_as_info
from db import save_entry

def run():
    # HTTP log
    http_ips = parse_access_log('access.log')
    for ip in http_ips:
        info = get_as_info(ip)
        save_entry(info['ip'], info['asn'], info['asn_desc'], 'http')

    # DNS log
    dns_ips = parse_dns_log('dns.log')
    for ip in dns_ips:
        info = get_as_info(ip)
        save_entry(info['ip'], info['asn'], info['asn_desc'], 'dns')
