import os
import socket
import struct
import select
import platform

if platform.system() == "Linux":
    import fcntl

def make_tun(name='tun0'):
    if platform.system() != "Linux":
        return None
    TUNSETIFF = 0x400454ca
    IFF_TUN = 0x0001
    IFF_NO_PI = 0x1000
    tun = os.open("/dev/net/tun", os.O_RDWR)
    ifr = struct.pack("16sH", name.encode(), IFF_TUN | IFF_NO_PI)
    fcntl.ioctl(tun, TUNSETIFF, ifr)
    return tun

def config_tun(name):
    os.system(f"ip addr add 10.8.0.2/30 dev {name}")
    os.system(f"ip link set {name} up")

def main():
    ip = input("Введи IP сервера (типа 192.168.1.123): ").strip()
    port = 60000
    is_linux = platform.system() == "Linux"
    tun = make_tun() if is_linux else None
    if is_linux and tun:
        config_tun("tun0")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((ip, port))
    print(f"[CLIENT] Подключено к {ip}:{port}")

    # ОТПРАВКА СИГНАЛА ПРИ ПОДКЛЮЧЕНИИ
    sock.send(b"HELLO_FROM_CLIENT")
    print("[CLIENT] >>> HELLO_FROM_CLIENT")

    while True:
        rlist = [sock]
        if tun: rlist.append(tun)
        r, _, _ = select.select(rlist, [], [])
        if tun and tun in r:
            try:
                data = os.read(tun, 1500)
                print(f"[CLIENT] >>> to server: {len(data)} bytes")
                sock.send(data)
            except Exception as e:
                print(f"[CLIENT] tun read/send error: {e}")
        if sock in r:
            try:
                data = sock.recv(1500)
                print(f"[CLIENT] <<< from server: {len(data)} bytes")
                print("[CLIENT] RAW DATA:", data)
                if tun:
                    os.write(tun, data)
            except Exception as e:
                print(f"[CLIENT] recv error: {e}")

if __name__ == "__main__":
    main()
