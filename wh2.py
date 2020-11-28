N, M = map(int, raw_input().split())
g= [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for p in range(M):
    a, b = map(int, raw_input().split())
    g[a].append(b)
    g[b].append(a)
q = []
q.append(1)
visited[1] = True

while q:
    q2 = []
    for node in q:
        for nb in g[node]:
            if not visited[nb]:
                visited[nb] = True
                q2.append(nb)
    q = q2
count = 0
for n in range(1, N + 1):
    if not visited[n]:
        print(n)
        count = 1
if count== 0:
    print('Connected')
