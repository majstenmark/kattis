import heapq
import math

N,M,S = map(int, raw_input().split())
g = [[] for _ in range(N)]
for m in range(M):
    u, v, t0, p, d = map(int, raw_input().split())
    g[v].append((u, t0, p, d))


T = N - 1
start = 0

def latestBus(arrivaltime, t0, P, d):
    departure = arrivaltime - d
    t = (departure - t0)/P
    #print('Arrivaltime {}, departure {}, t {}'.format(arrivaltime, departure, t))
    return t >= 0, t0 + t*P

def travel():
    # Dijkstra from T to S
    INF = 10**12
    dist = [-INF for _ in range(N)]

    pq = []
    dist[T] = S
    pq.append((-S, T))
    heapq.heapify(pq)
    while pq:
        (nd, node) = heapq.heappop(pq)
        if node == 0:
            return dist[node] >= 0, dist[node]
        for u,t0, P,d in g[node]:
            ok, alt = latestBus(dist[node], t0, P, d)
        #    print('Travel from u {} to {} OK {}, alt {}'.format(u, node, ok, alt))
            if not ok:
                continue
            if dist[u] < alt:
                dist[u] = alt
                heapq.heappush(pq, (-dist[u], u))
    return False, dist[0]

ok, time = travel()
if not ok:
    print('impossible')
else:
    print(time)
