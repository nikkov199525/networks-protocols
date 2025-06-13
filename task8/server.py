import os
import socket
import fcntl
import struct
import select

def make_tun(name='tun0'):
    TUNSETIFF = 0x400454ca
    IFF_TUN = 0x0001
    IFF_NO_PI = 0x1000
    tun = os.open("/dev/net/tun", os.O_RDWR)
    ifr = struct.pack("16sH", name.encode(), IFF_TUN | IFF_NO_PI)
    fcntl.ioctl(tun, TUNSETIFF, ifr)
    return tun

def config_tun(name):
    os.system(f"ip addr add 10.8.0.1/30 dev {name}")
    os.system(f"ip link set {name} up")

def main():
    try:
        import ipaddress
        ip_input = input("IP: ").strip()
        ip = str(ipaddress.ip_address(ip_input))
    except Exception:
        print("Невалидный IP, слушаю на 0.0.0.0")
        ip = "0.0.0.0"

    port = int(input("Port: ").strip())
    tun = make_tun()
    config_tun("tun0")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    print(f"VPN server running at {ip}:{port}")

    client_addr = None

    while True:
        rlist, _, _ = select.select([tun, sock], [], [])
        if sock in rlist:
            try:
                data, client_addr = sock.recvfrom(1500)
                print(f"[SERVER] <<< from {client_addr}: {len(data)} bytes")
                os.write(tun, data)
                if client_addr:
                    test_msg = b'VPN_OK_BACK'
                    sock.sendto(test_msg, client_addr)
                    print(f"[SERVER] >>> test reply to {client_addr}: {test_msg}")
            except Exception as e:
                print(f"[SERVER] recv/send error: {e}")

        if tun in rlist:
            data = os.read(tun, 1500)
            if client_addr:
                print(f"[SERVER] >>> to {client_addr}: {len(data)} bytes")
                try:
                    sock.sendto(data, client_addr)
                except Exception as e:
                    print(f"[SERVER] sendto error: {e}")
            else:
                print("[SERVER] !!! Нет client_addr, пакет из tun игнорируется")

if __name__ == "__main__":
    main()