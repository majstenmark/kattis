
INF = 1000000000
MINF = - INF
IMPOSSIBLE = 'Impossible'
MININF = '-Infinity'

N, M, Q = map(int, raw_input().split())
while (N, M, Q) != (0, 0, 0):
    dist = [[INF]*N for _ in range(N)]
    for n in range(N):
        dist[n][n] = 0
    edgs = [tuple(map(int, raw_input().split())) for _ in range(M)]
    def bfs(s, g):
        visited = set()
        q = [s]
        for node in q:
            visited.add(node)
        while q:
            q2 = []
            for node in q:
                for ne in g[node]:
                    if ne not in visited:
                        visited.add(ne)
                        q2.append(ne)
            q = q2
        return visited

    def setInf(fromNodes, toNodes, dist):
        for fn in fromNodes:
            for tn in toNodes:
                dist[fn][tn] = MINF

    graph = [[] for _ in range(N)]
    backgraph = [[] for _ in range(N)]
    for e in edgs:
        dist[e[0]][e[1]] = min(dist[e[0]][e[1]], e[2])
        graph[e[0]].append(e[1])
        backgraph[e[1]].append(e[0])

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j] and max(dist[k][j], dist[i][k]) < INF:
                    dist[i][j] = dist[i][k] + dist[k][j]
                #    nxt[i][j] = nxt[i][k]
    for n in range(N):
        if dist[n][n] < 0:
            forward = bfs(n, graph)
            backward = bfs(n, backgraph)
            setInf(backward, forward, dist)

    queries = [map(int, raw_input().split()) for _ in range(Q)]
    for u, v in queries:
        d = dist[u][v]
        if d == MINF:
            print(MININF)
        elif d == INF:
            print(IMPOSSIBLE)
        else:
             print d
    print('')
    N, M, Q = map(int, raw_input().split())
