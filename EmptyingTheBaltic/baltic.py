from collections import defaultdict as ddict
import heapq

h, w = map(int, raw_input().split())
mapping = [map(int, raw_input().split()) for _ in range(h)]
i, j = map(lambda x: int(x) - 1, raw_input().split())

g = ddict(list)
for r in range(h):
    for c in range(w):
        nbs = [(r - 1, c), (r + 1, c), (r, c - 1),(r , c + 1),
        (r + 1 , c + 1),(r - 1 , c + 1),(r+1 , c - 1),(r -1 , c - 1)]
        for nr, nc in nbs:
            if 0 <= nr < h and 0 <= nc < w and mapping[nr][nc] < 0:
                g[(r, c)].append((nr, nc))


pq = []
dist = ddict(int)
dist[(i, j)] = mapping[i][j]
pq.append((mapping[i][j], (i, j)))
heapq.heapify(pq)
done = False
water = 0
while pq:
    (nd, node) = heapq.heappop(pq)
    water -= nd
    for nn in g[node]:
        alt = max(dist[node], mapping[nn[0]][nn[1]])
    #    s = '({}, {}) h {} dist {}'.format(nn[0], nn[1], mapping[nn[0]][nn[1]], dist[node])
    #    print(s)
        if dist[nn] > alt:
            dist[nn] = alt
        #    s = 'Updated ({}, {}) dist {}'.format(nn[0], nn[1], dist[nn])

        #    print(s)
            heapq.heappush(pq, (dist[nn], nn))

print(water)
