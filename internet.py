import sys
sys.setrecursionlimit(200000)
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

visited = set()
def dfs(u):
    visited.add(u)
    for v in G[u]:
        if v not in visited:
            dfs(v)

dfs(0)
for i in range(N):
    if i not in visited:
        print(i+1)
if len(visited) == N:
    print('Connected')

def bfs(q, g):
    visited = [False] * N
    for node in q:
        visited[node] = True
    while q:
        q2 = []
        for node in q:
            for ne in g[node]:
                if not visited[ne]:
                    visited[ne] = True
                    q2.append(ne)
        q = q2
    return visited