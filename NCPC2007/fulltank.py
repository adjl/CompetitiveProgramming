n, m = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
grid = [[] for _ in range(n)]
for _ in range(int(m)):
    u, v, d = [int(i) for i in input().split()]
    grid[u][v] = d  # grid[v][u] = d?
for _ in range(int(input())):
    c, s, e = [int(i) for i in input().split()]
    cheapest = []
    for u in range(n):
        for v in range(len(grid[u])):
            cheapest[u][v] = 10000
    city = s
    while city != e:
        for road in range(len(grid[city])):
            d = grid[city][road]
            if d > c:
                continue
            price = p[city] * d
            if price < cheapest[city][road]:
                cheapest[city][road] = price
