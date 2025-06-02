import socket
import random
import time

target_ip = '192.168.1.219' # ip нужно поменять на свой, узнается как обычно через ipconfig
ports = list(range(20, 1025))
random.shuffle(ports)

for port in ports:
    # TCP scan
    try:
        sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_tcp.settimeout(0.2)
        result = sock_tcp.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port}/TCP is OPEN")
        sock_tcp.close()
    except Exception as e:
        pass

    # UDP scan
    try:
        sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock_udp.settimeout(0.2)
        sock_udp.sendto(b'test', (target_ip, port))
        print(f"[+] Sent UDP packet to port {port}")
        sock_udp.close()
    except Exception as e:
        pass

    time.sleep(random.uniform(0.01, 0.15))
