def bfs(q, g, goal):
    visited = [False] * F
    layer = 0
    for node in q:
        visited[node] = True
    while q:
        q2 = []
        for node in q:
            if node == goal:
                return layer
            for ne in g[node]:
                if not visited[ne]:
                    visited[ne] = True
                    q2.append(ne)
        q = q2
        layer += 1
    return -1

F, Si, Gi, U, D = map(int, raw_input().split())
S = Si -1
G = Gi - 1
g = [[] for _ in range(F)]
for floor in range(F):
    up = floor if floor + U >= F else floor + U
    down = floor if floor -D < 0 else floor -D
    g[floor].append(up)
    g[floor].append(down)

q = [S]
k = bfs(q, g, G)
if k == -1:
    print 'use the stairs'
else:
    print k
