import heapq

N = int(raw_input())
graph = [[] for _ in range(N + 1)]
start = 1
end = N
INF = 10**12
dist = [INF for _ in range(N + 1)]
items = map(int, raw_input().split())
m = int(raw_input())
prev = [(0,items[0]) for _ in range(N + 1)]
for edge in range(m):
    a, b, d = map(int, raw_input().split())
    graph[a].append((b, d))
    graph[b].append((a,d))
# Dijkstra
pq = []
dist[start] = 0
pq.append((0, start))
heapq.heapify(pq)
while pq:
    (nd, node) = heapq.heappop(pq)
    for (nn, dd) in graph[node]:

        alt = dist[node] + dd

        if dist[nn] > alt:
            dist[nn] = alt
            prev[nn] = (node, prev[node][1] + items[nn - 1])
            heapq.heappush(pq, (dist[nn], nn))
        elif dist[nn] == alt and prev[nn][1] < prev[node][1] + items[nn - 1]:
            prev[nn] = (node, prev[node][1] + items[nn - 1])
            heapq.heappush(pq, (dist[nn], nn))
if dist[end] < INF:

    s = '{} {}'.format(dist[end], prev[end][1])
    print(s)
else:
    print('impossible')
