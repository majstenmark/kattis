import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

import heapq
INF = 10**30
    

def dij(S, g):
    #g list with lists with tuples distance, other node
    # Dijkstra from S. Check t optionally
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


V, E, C, K, M = nl()
g = [[] for _ in range(V)]
for e in range(E):
    u, v, w = nl()
    g[u-1].append((w, v-1))
    g[v-1].append((w, u-1))
f = nl()
dist = dij(0, g)
clearings = []
for x in f:
    if dist[x-1] < INF:
        clearings.append(dist[x-1])
clearings.sort()
#print(clearings)
needed = min(M, K)
if len(clearings) < needed:
    print(-1)
else:
    print(2 * clearings[needed-1])