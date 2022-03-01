import heapq
import sys
from collections import defaultdict as dd

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())


def dij(S, g):
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
        #if node == T: return dist[T]
        for (dd, nn) in g[node]:
            alt = dist[node] + dd
            if dist[nn] > alt:
                dist[nn] = alt
                heapq.heappush(pq, (dist[nn], nn))

    return dist

N, V, E = nl()
edges = [nl() for _ in range(E)]
g = [[] for _ in range(V)]
for u, v, w in edges:
    g[u].append((w, v))
    g[v].append((w, u))
G = dd(dict)
for n in range(N):
    dist = dij(n, g)
    for n2 in range(N):
        G[n][n2] = dist[n2]

dp = {} #nodeid, mask
def opt(nid, mask):
    if (nid, mask) in dp:
        return dp[nid, mask]
    if mask == 0:
        if nid == 0: return 0
        return 10**10
    best = 10**10
    for u in range(N):
        if (1<<u) & mask:
            best = min(best, G[nid][u] + opt(u, mask ^ (1<<u)))
    dp[nid, mask] = best
    return best

print(opt(0, (1<<N) - 1))
