import heapq
# Dijkstra from S to T
INF = 10**12
def dij(x, cap):
    dist = [INF for _ in range(N)]
    T = N -1
    pq = []
    dist[0] = 0
    pq.append((0, 0))
    heapq.heapify(pq)
    done = False
    ok = False
    while pq and not done:
        (nd, node) = heapq.heappop(pq)
        if node == T: 
            done = True
            if dist[T] <= x: ok = True
        for (dd, nn) in g[node]:
            if dd <= cap:
                alt = dist[node] + dd
                if dist[nn] > alt:
                    dist[nn] = alt
                    heapq.heappush(pq, (dist[nn], nn))

    return ok, dist[T]

N, M, X = [int(v) for v in raw_input().split()]
g = [[] for _ in range(N)]
maxw = 0
minw = 0
for _ in range(M):
    a, b, c = [int(v) for v in raw_input().split()]
    g[a-1].append((c, b-1))
    g[b-1].append((c, a-1))
    maxw = max(maxw, c)

_, shortest = dij(INF, INF)

Xp = (1 + X/100.0) * shortest
#print(shortest, Xp)
cnt = 0
while cnt < 30 and minw < maxw -1:
    midcap = (maxw + minw)/2
    ok, _ = dij(Xp, midcap)
    #print('testing {} {} {} {}'.format(midcap, ok, minw, maxw))
    if ok:
        maxw = midcap
    else:
        minw = midcap
    cnt +=1
print(maxw)
