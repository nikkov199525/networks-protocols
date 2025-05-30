import heapq

class Router:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.routes = {}

    def connect(self, other, cost, pref):
        self.neighbors[other] = (cost, pref)

    def update_routes(self, all_routers):
        dist = {r: (float('inf'), float('inf')) for r in all_routers}
        prev = {}
        dist[self] = (0, 0)
        heap = [(0, 0, self)]
        while heap:
            pref, cost, curr = heapq.heappop(heap)
            for neighbor, (n_cost, n_pref) in curr.neighbors.items():
                tot_pref = pref + n_pref
                tot_cost = cost + n_cost
                if (tot_pref, tot_cost) < dist[neighbor]:
                    dist[neighbor] = (tot_pref, tot_cost)
                    prev[neighbor] = curr
                    heapq.heappush(heap, (tot_pref, tot_cost, neighbor))
        self.routes = {}
        for r in all_routers:
            if r is self or r not in prev: continue
            nh = r
            while prev[nh] is not self:
                nh = prev[nh]
            self.routes[r.name] = (nh.name, dist[r][1], dist[r][0])

    def print_routes(self):
        print(f'\nМаршруты {self.name}:')
        print('Назначение  След.хоп  Стоимость  Преференс')
        for dst, (nh, c, p) in sorted(self.routes.items()):
            print(f'{dst:<11} {nh:<9} {c:<10} {p:<10}')

    def send_packet(self, dst_name, all_routers):
        print(f'\nОтправка пакета от {self.name} к {dst_name}')
        path, curr = [self.name], self
        cost_sum, pref_sum = 0, 0
        while curr.name != dst_name:
            route = curr.routes.get(dst_name)
            if not route:
                print(f'{curr.name}: Нет маршрута к {dst_name}')
                return
            nh_name, c, p = route
            cost_sum += c
            pref_sum += p
            print(f'{curr.name} → {nh_name} (стоим. {c}, преф. {p})')
            next_r = next(r for r in curr.neighbors if r.name == nh_name)
            curr = next_r
            path.append(curr.name)
        print(f'Доставлено! Путь: {" → ".join(path)}')
        print(f'Общая стоимость: {cost_sum}, предпочтение: {pref_sum}')
        print("\nАльтернативные маршруты до", dst_name)
        print(f'{"Роутер":<10} {"След.хоп":<10} {"Преференс":<12} {"Стоимость":<10}')
        for router in all_routers:
            route = router.routes.get(dst_name)
            if route:
                nh, c, p = route
                print(f'{router.name:<10} {nh:<10} {p:<12} {c:<10}')

r1, r2, r3, r4, r5, r6 = [Router(f'R{i}') for i in range(1,7)]
r1.connect(r2, 1, 10); r2.connect(r1, 1, 10)
r2.connect(r3, 2, 5);  r3.connect(r2, 2, 5)
r3.connect(r6, 1, 10); r6.connect(r3, 1, 10)
r1.connect(r4, 5, 5);  r4.connect(r1, 5, 5)
r4.connect(r5, 1, 2);  r5.connect(r4, 1, 2)
r5.connect(r6, 2, 3);  r6.connect(r5, 2, 3)
routers = [r1, r2, r3, r4, r5, r6]
for r in routers: r.update_routes(routers)
print("=== До изменения ===")
for r in routers: r.print_routes()
print("\n=== Отправка R1 → R6 ===")
r1.send_packet('R6', routers)
r4.neighbors[r5] = (1, 50)
r5.neighbors[r4] = (1, 50)
for r in routers: r.update_routes(routers)
print("\n=== После изменения ===")
for r in routers: r.print_routes()
print("\n=== Отправка R1 → R6 (после изменений) ===")
r1.send_packet('R6', routers)
