import heapq
from collections import defaultdict as dd

def dijkstra(S):
    # Dijkstra from S to T
   
    dist = {l:(INF, INF) for l in L}
    pq = []
    dist[S] = (0, 0)
    pq.append((0, 0, S))
    heapq.heapify(pq)
    while pq:
        (level, nd, node) = heapq.heappop(pq)
        for (dd, nn) in g[node]:
            alt_lvl = dist[node][0] + 1
            alt_dist = dd
            if alt_lvl < dist[nn][0]:
                dist[nn] = (alt_lvl, dd)
                heapq.heappush(pq, (alt_lvl, dist[nn], nn))
            elif alt_lvl == dist[nn][0] and alt_dist < dist[nn][1]:
                dist[nn] = (alt_lvl, dd)
                heapq.heappush(pq, (alt_lvl, dist[nn], nn))

    return dist
INF = 10**12
N, M = [int(v) for v in raw_input().split()]
L = raw_input().split()

g = dd(list)
for m in range(M):
    l1, l2, cs = raw_input().split()
    c = int(cs)
    g[l1].append((c, l2))
    g[l2].append((c, l1))
    
dist = dijkstra('English')

cost = 0
for l in L:
    #print('{} {}'.format(l, dist[id]))
    cost += dist[l][1]
if cost > INF:
    print('Impossible')
else:
    print(cost)