from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s):
    sys.stderr.write('{}\n'.format(s))

def ni():
    return int(inp())

def nl():
    return [int(_) for _ in inp().split()]

N, K = nl()

G = [nl() for _ in range(N)]

gridpts = defaultdict(list)

for i in range(N):
    for j in range(N):
        gridpts[G[i][j]].append((i, j))

INF = 10**18
dist = defaultdict(lambda: INF)
for x, y in gridpts[1]:
    dist[x, y] = 0

for cnt in range(1, K):
    for x, y in gridpts[cnt]:
        d = dist[x, y]
        for x2, y2 in gridpts[cnt+1]:
            dist[x2, y2] = min(dist[x2, y2], d + abs(x - x2) + abs(y - y2))
OUT = INF
for x, y in gridpts[K]:
    OUT = min(OUT, dist[x, y])
if OUT == INF: OUT = -1
print(OUT)

