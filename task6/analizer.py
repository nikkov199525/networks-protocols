from scapy.all import sniff, TCP, UDP, IP, get_if_list
from collections import defaultdict
import time
import threading

SCAN_TIME_WINDOW = 3
SCAN_THRESHOLD = 10
scans = defaultdict(list)

iface_list = get_if_list()
print("Интерфейсы для мониторинга:", iface_list)

def worker(iface):
    try:
        while True:
            packets = sniff(filter="tcp or udp", count=1, store=1, iface=iface)
            for packet in packets:
                if packet.haslayer(IP) and (packet.haslayer(TCP) or packet.haslayer(UDP)):
                    src_ip = packet[IP].src
                    proto = ""
                    dst_port = None
                    if packet.haslayer(TCP):
                        proto = "TCP"
                        dst_port = packet[TCP].dport
                    elif packet.haslayer(UDP):
                        proto = "UDP"
                        dst_port = packet[UDP].dport
                    current_time = time.time()
                    key = (src_ip, proto, iface)
                    scans[key].append((dst_port, current_time))
                    scans[key] = [(port, t) for port, t in scans[key] if current_time - t < SCAN_TIME_WINDOW]
                    recent_ports = [port for port, t in scans[key]]
                    if len(set(recent_ports)) > SCAN_THRESHOLD:
                        print("\n==============================================")
                        print("Обнаружена аномалия!")
                        print(f"Интерфейс: {iface}")
                        print(f"Источник: {src_ip}")
                        print(f"Протокол: {proto}")
                        print(f"Время: {time.strftime('%H:%M:%S')}")
                        print(f"Просканированные порты: {sorted(set(recent_ports))}")
                        print(f"Количество портов: {len(set(recent_ports))} за {SCAN_TIME_WINDOW} секунд")
                        print("==============================================\n")
                        scans[key] = []
    except KeyboardInterrupt:
        pass
threads = []
for iface in iface_list:
    t = threading.Thread(target=worker, args=(iface,), daemon=True)
    t.start()
    threads.append(t)
print("Для завершения нажмите Ctrl+C")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nПрограмма остановлена пользователем.")
