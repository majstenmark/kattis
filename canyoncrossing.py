import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop
#NOT SUBMITTED
itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

R, C, K = nl()
grid = [nl() for _ in range(R)]
tot = R * C
g = [[] for _ in range(tot)]
H = [0] * tot

def toid(r, c):
    return r * R + c

def get4nb(r, c, rmin = 0, rmax = M, cmin = 0, cmax = N):
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    nb = []
    for dr, dc in diff:
        if rmin <= r + dr < rmax and cmin <= c + dc < cmax:
            nb.append((r+dr, c + dc))
    return nb 

for r in range(R):
    for c in range(C):
        id = toid(r, c)
        H[id] = grid[r][c]
        nbs = get4nb(r, c)
        for n in nbs:
            i = toid(n[0], n[1])
            g[id].append(i)


def bfs(q, g, mn):
    visited = [False] * tot
    cnt = [0] * tot
    for node in q:
        visited[node] = True
        if H[node] <= mn:
            cnt[node] = 1

    while q:
        q2 = []
        for node in q:
            for ne in g[node]:
                if not visited[ne]:
                    visited[ne] = True
                    q2.append(ne)
        q = q2
    return visited

