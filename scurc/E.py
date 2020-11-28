import math
from heapq import *
def d2(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**.5 - p1[2] - p2[2]
n = input()
pts = [map(float, raw_input().split()) for _ in range(n)]
p = [i for i in range(n)]
sz = [1]*n
tot = 0.0

INF = 10**18
dist = [10**18]*n
dist[0] = 0
heap = []
heappush(heap, (0.0, 0))
V = set()
X = 0
for _ in range(n):
    d, i = heappop(heap)
    while i in V:
        d, i = heappop(heap)
    X += d
    V.add(i)
    for j in xrange(n):
        if j not in V:
            d = d2(pts[i], pts[j])
            if d < dist[j]:
                dist[j] = d
                heappush(heap, (d, j))

print(X)
