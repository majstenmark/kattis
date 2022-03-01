import sys
from collections import defaultdict as dd

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

M, N = nl()
Hs = [nl() for _ in range(M)]
tot = N*M
g = [[] for _ in range(tot)]
H = [0] * tot

def toid(r, c):
    return r * N + c

def get4nb(r, c, rmin = 0, rmax = M, cmin = 0, cmax = N):
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    nb = []
    for dr, dc in diff:
        if rmin <= r + dr < rmax and cmin <= c + dc < cmax:
            nb.append((r+dr, c + dc))
    return nb 

for r in range(M):
    for c in range(N):
        id = toid(r, c)
        H[id] = Hs[r][c]


for r in range(M):
    for c in range(N):
        id = toid(r, c)
        nbs = get4nb(r, c)
        for n in nbs:
            i = toid(n[0], n[1])
            h1 = H[id]
            h2 = H[i]
            diff = max(0, h2 - h1)
            
            g[id].append((diff, i))

import heapq

def dij(S, T, g):
    #g list with lists with tuples distance, other node
    # Dijkstra from S. Check t optionally
    INF = 10**12
    N = len(g)
    dist = [INF for _ in range(N)]

    pq = []
    dist[S] = 0
    pq.append((0, S))
    heapq.heapify(pq)
    done = False
    while pq and not done:
        (nd, node) = heapq.heappop(pq)
        if node == T: return dist[T]
        for (dd, nn) in g[node]:
            alt = max(nd, dd)
            if dist[nn] > alt:
                dist[nn] = alt
                heapq.heappush(pq, (dist[nn], nn))

    return dist

d = dij(0, tot-1, g)
print(d)
    