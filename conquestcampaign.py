import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def nl1(): return [int(v)-1 for v in inp().split()]
def ni(): return int(inp())

R, C, N = nl()
weak = [tuple(nl1()) for _ in range(N)]

def get4nb(r, c):
    rmin = 0
    rmax = R
    cmin = 0
    cmax = C
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    nb = []
    for dr, dc in diff:
        if rmin <= r + dr < rmax and cmin <= c + dc < cmax:
            nb.append((r+dr, c + dc))
    return nb 

def bfs(q):
    visited = set()
    for node in q:
        visited.add(node)
    cnt = 0
    while q:
        cnt += 1
        q2 = []
        for node in q:
            for ne in get4nb(node[0], node[1]):
                if ne not in visited:
                    visited.add(ne)
                    q2.append(ne)
        q = q2
        
    return cnt

print(bfs(weak))