from db import init_db, mark_as_nsdni
from run_pipeline import run
from get_nsdni_ips import resolve_nsdni_hosts
import threading, os, time, sys

def launch_server():
    os.system(f'{sys.executable} app.py')

def launch_dns():
    os.system(f'{sys.executable} dns_server.py')

if __name__ == '__main__':
    init_db()
    run()
    for ip in resolve_nsdni_hosts():
        mark_as_nsdni(ip)

    threading.Thread(target=launch_dns, daemon=True).start()
    threading.Thread(target=launch_server, daemon=True).start()

    print("Сервер запущен на http://localhost:8000")
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        print("\nОстановка.")
