import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
grid = [inp() for _ in range(N)]
start = 0, 0
for r in range(N):
    for c in range(N):
        if grid[r][c] == 'K':
            start = r, c


def nb(node):
    r, c = node
    rmin = 0
    rmax = N
    cmin = 0
    cmax = N
    diff = [(r+2,c+1), (r+2,c-1), (r-2,c+1), (r-2,c-1), (r+1,c+2), (r+1,c-2), (r-1,c+2), (r-1,c-2)]
    nb = []
    for rr, cc in diff:
        if rmin <= rr < rmax and cmin <= cc < cmax:
            nb.append((rr, cc))
    return nb 


def bfs(q, T):
    visited = set()
    for node in q:
        visited.add(node)
    cnt = 0
    while q:
        q2 = []
        for node in q:
            if node == T:
                return cnt
            
            for ne in nb(node):
                if ne not in visited and grid[ne[0]][ne[1]] != '#':
                    visited.add(ne)
                    q2.append(ne)
        q = q2
        cnt += 1
    return -1

steps = bfs([start], (0, 0))
print(steps)