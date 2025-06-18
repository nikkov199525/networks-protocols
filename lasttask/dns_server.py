import socketserver, time

LOG = "dns_live.log"

class DNSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, sock = self.request
        ip = self.client_address[0]
        if len(data) < 12:
            return
        qname = data[12:]
        qname_parts = []
        while qname:
            length = qname[0]
            if length == 0:
                break
            qname_parts.append(qname[1:1+length].decode(errors='ignore'))
            qname = qname[1+length:]
        domain = ".".join(qname_parts)
        ts = int(time.time())
        with open(LOG, "a") as f:
            f.write(f"{ip},{domain},{ts}\n")
        # reply with minimal empty response
        response = data[:2] + b"\x81\x80" + data[4:6] + data[4:6] + b"\x00\x00\x00\x00" + data[12:]
        sock.sendto(response, self.client_address)

if __name__ == "__main__":
    with socketserver.UDPServer(("0.0.0.0", 53), DNSHandler) as server:
        print("DNS сервер запущен на порту 53...")
        server.serve_forever()