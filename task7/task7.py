class Bridge:
    def __init__(self, bridge_id, priority=32768):
        self.bridge_id = bridge_id
        self.priority = priority
        self.mac = bridge_id
        self.bid = (priority << 48) + self.mac
        self.neighbors = {}
        self.ports = {}
        self.root_id = self.bid
        self.path_cost = 0
        self.root_port = None

    def connect(self, neighbor, port_id, cost):
        self.neighbors[neighbor] = (port_id, cost)
        self.ports[port_id] = {"neighbor": neighbor, "cost": cost, "role": None}

    def stp_step(self, bridges, log=False):
        root = min(bridges, key=lambda b: b.bid)
        self.root_id = root.bid
        if self is root:
            self.path_cost = 0
            self.root_port = None
        else:
            best = None
            for port_id, info in self.ports.items():
                neighbor = info["neighbor"]
                cost = info["cost"]
                total_cost = neighbor.path_cost + cost
                neighbor_bid = neighbor.bid
                pid = port_id
                candidate = (total_cost, neighbor_bid, pid)
                if best is None or candidate < best[1]:
                    best = (port_id, candidate)
            if best:
                self.root_port = best[0]
                self.path_cost = best[1][0]
        for port_id, info in self.ports.items():
            if self.root_port and port_id == self.root_port:
                info["role"] = "Root Port"
            else:
                info["role"] = None
        for port_id, info in self.ports.items():
            neighbor = info["neighbor"]
            neighbor_port_id = [pid for pid, pi in neighbor.ports.items() if pi["neighbor"] is self]
            if neighbor_port_id:
                n_port_id = neighbor_port_id[0]
                my_tuple = (self.path_cost, self.bid, port_id)
                neighbor_tuple = (neighbor.path_cost, neighbor.bid, n_port_id)
                if my_tuple < neighbor_tuple:
                    info["role"] = "Designated Port"
                elif info["role"] is None:
                    info["role"] = "Blocked"

    def print_ports(self):
        print(f"\nBridge {self.bridge_id}, BID={self.bid}")
        print(f"  Root ID: {self.root_id}, Path cost: {self.path_cost}")
        if self.root_port:
            print(f"  Root Port: Port {self.root_port}")
        else:
            print("  Root Port: ---")
        for port_id, info in sorted(self.ports.items()):
            neighbor = info["neighbor"].bridge_id
            print(f"  Port {port_id} (to {neighbor}): Cost={info['cost']}, Role={info['role']}")

b1 = Bridge(1)
b2 = Bridge(2)
b3 = Bridge(3)
b4 = Bridge(4)
b5 = Bridge(5)
b6 = Bridge(6)
b1.connect(b2, 1, 4); b2.connect(b1, 1, 4)
b2.connect(b3, 2, 4); b3.connect(b2, 1, 4)
b3.connect(b4, 2, 4); b4.connect(b3, 1, 4)
b4.connect(b5, 2, 4); b5.connect(b4, 1, 4)
b5.connect(b6, 2, 4); b6.connect(b5, 1, 4)
b6.connect(b1, 2, 4); b1.connect(b6, 2, 4)
b3.connect(b6, 3, 10); b6.connect(b3, 3, 10)
bridges = [b1, b2, b3, b4, b5, b6]
for step in range(5):
    for br in bridges:
        br.stp_step(bridges, log=False)
print("=== Финальное состояние ===")
for br in bridges:
    br.print_ports()
