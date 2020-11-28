from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop
inp = raw_input

def nl():
    return [int(v) for v in inp().split()]

def inf(): return 10 ** 30

def solve(stones, bp, gz):
    q = [(0, bp)]
    dist = dd(inf)
    dist[bp] = 0
    while q:
        d, st = pop(q)
        for w, p in stones[st]:
            if p + d < dist[w]:
                dist[w] = p + d
                push(q, (dist[w], w))
    return dist[gz]

n = int(inp())
while n != 0:
    stones = dd(list)
    for _ in range(n):
        a, b, h = nl()
        price = (a + b ) * h
        stones[a].append((b, price))
        stones[b].append((a, price))

    bp, gz = nl()
    r = solve(stones, bp, gz)
    print('{}.{:02d}'.format(r//100, r%100))

    n = int(inp())