import heapq
# Dijkstra from S to T
def dji(g):
    INF = 10**12
    dist = [[INF for _ in range(N)] for _ in range(2**7)]

    pq = []
    dist[0][0] = 0
    pq.append((0, 0, 0))
    heapq.heapify(pq)

    while pq:
        (dist_to_node, colors_on_path, node) = heapq.heappop(pq)
        for road_dist, road_color, neigh in g[node]:
            altDist = dist_to_node + road_dist
            altColors = colors_on_path | road_color
            if dist[altColors][neigh] > altDist:
                dist[altColors][neigh] = altDist
                heapq.heappush(pq, (altDist, altColors, neigh))

    return dist[2 ** 7 -1][0]

N, M = map(int, raw_input().split())
colors = {'R': 1,
'O': 2,
'Y': 4,
'G': 8,
'B': 16,
'I': 32,
'V': 64}
g= [[] for _ in range(N)]
for m in range(M):
      line = raw_input().split()
      u = int(line[0]) -1
      v = int(line[1]) -1
      d = int(line[2])
      c = colors[line[3]]
      g[u].append((d, c, v))
      g[v].append((d, c, u))
print dji(g)
