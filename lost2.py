from collections import defaultdict as dd
from heapq import heappop as pop, heappush as push

g = dd(list)
N, M = [int(v) for v in raw_input().split()]
L = raw_input().split()
edges = []

for m in range(M):
    l1, l2, cs = raw_input().split()
    c = int(cs)
    g[l1].append((c, l2))
    g[l2].append((c, l1))

visited = set(['English'])
q = ['English']
edges = []
for c, n in g['English']:
    push(edges, (0, c, n))

cost = 0
while edges:
    lvl, c, n = pop(edges)
    if n not in visited:
        cost += c
        visited.add(n)
        for cc, nn in g[n]:
            push(edges, (lvl + 1, cc, nn))
    

if len(visited) < N + 1:
    print('Impossible')
else:
    print(cost)