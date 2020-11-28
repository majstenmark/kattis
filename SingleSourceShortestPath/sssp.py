import heapq
line = raw_input()
while line != '0 0 0 0':
    N, M, Q, S = map(int, line.split())

    g = [[] for _ in range(N)]
    for m in range(M):
        u, v , w = map(int, raw_input().split())
        g[u].append((w, v))
    #    g[v].append((w, u))

    INF = 10**12
    dist = [INF for _ in range(N)]

    pq = []
    dist[S] = 0
    pq.append((0, S))
    heapq.heapify(pq)
    done = False
    while pq and not done:
        (nd, node) = heapq.heappop(pq)
        for (dd, nn) in g[node]:
            alt = dist[node] + dd
            if dist[nn] > alt:
                dist[nn] = alt
                heapq.heappush(pq, (dist[nn], nn))

    for q in range(Q):
        T = int(raw_input())
        print(dist[T] if dist[T] != INF else 'Impossible')
    print('')
    line = raw_input()
