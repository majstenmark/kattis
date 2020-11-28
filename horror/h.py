N, H, L = map(int, raw_input().split())
dist = [-1 for _ in range(N)]

h_list = map(int, raw_input().split())

q = []
for h in h_list:
    dist[h] = 0
    q.append(h)
graph = [[] for _ in range(N)] #connections
for i in range(L):
    a, b = map(int, raw_input().split())
    graph[a].append(b)
    graph[b].append(a)


while q:
    q2 =[]
    for n in q:
        for nn in graph[n]:
            if dist[nn] == -1:
                dist[nn] = dist[n] + 1
                q2.append(nn)
    q = q2

index = 0
maxdist = -1
for n in range(N):
    if dist[n] > maxdist:
        index = n
        maxdist = dist[n]
    if dist[n] == -1:
        index = n
        break
print(index)
