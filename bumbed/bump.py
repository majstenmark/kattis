import heapq

N, M, F, S, T = map(int, raw_input().split())
g = [[] for e in range(2*N)]
INF = 10**12
dist = [INF for e in range(2*N)]
for m in range(M):
    i,j,c = map(int, raw_input().split())
    g[i].append((c, j))
    g[j].append((c, i))
    g[i + N].append((c, j+N))
    g[j+N].append((c, i+N))
for f in range(F):
    u, v = map(int, raw_input().split())
    g[u].append((0, v + N))
# Dijstra from S to T
# Dijkstra
g[T].append((0,T + N))
pq = []
dist[S] = 0
pq.append((0, S))
heapq.heapify(pq)
done = False
while pq and not done:
    (nd, node) = heapq.heappop(pq)
    if node == T + N: done= True
    for (dd, nn) in g[node]:

        alt = dist[node] + dd

        if dist[nn] > alt:
            dist[nn] = alt
            heapq.heappush(pq, (dist[nn], nn))

s = '{}'.format(dist[T + N])
print(s)
