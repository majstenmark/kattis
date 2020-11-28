import heapq
office = 1
home = 2

# Dijkstra from S to T
INF = 10**12
def dij(g):
    dist = [INF for _ in range(len(g))]

    pq = []
    dist[home] = 0
    pq.append((0, home))
    heapq.heapify(pq)
    done = False
    while pq and not done:
        (nd, node) = heapq.heappop(pq)
        if node == office: done= True
        for (dd, nn) in g[node]:
            alt = dist[node] + dd
            if dist[nn] > alt:
                dist[nn] = alt
                heapq.heappush(pq, (dist[nn], nn))
    return dist

def countPaths(dist, g):
    nbrOfPaths=[0 for _ in range(len(g))]
    nbrOfPaths[home] = 1

    sortedDist = sorted(enumerate(dist), key = lambda x: x[1])
    for node, d in sortedDist:

        for d2, ne in g[node]:
            if dist[node] < dist[ne]:
                nbrOfPaths[ne] += nbrOfPaths[node]
    return nbrOfPaths[office]


line = raw_input()
while line != '0':
    N , M = map(int, line.split())
    g = [[] for _ in range(N + 1)]
    for m in range(M):
        a, b, d = map(int, raw_input().split())
        g[a].append((d, b))
        g[b].append((d,a))
    distMat = dij(g)
    paths = countPaths(distMat,  g)
    print(paths)

    line = raw_input()
