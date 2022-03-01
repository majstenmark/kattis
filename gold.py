import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

W, H = nl()
grid = [inp() for _ in range(H)]
draft = set()
start = 0, 0

def get4nb(r, c):
    rmin = 0
    rmax = len(grid)
    cmin = 0
    cmax = len(grid[0])
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    nb = []
    for dr, dc in diff:
        if rmin <= r + dr < rmax and cmin <= c + dc < cmax:
            nb.append((r+dr, c + dc))
    return nb 


for r in range(H):
    for c in range(W):
        if grid[r][c] == 'P':
            start = r, c
        if grid[r][c] == 'T':
            for ne in get4nb(r, c):
                draft.add(ne)

def dfs(start, visited):
    r, c= start
    visited.add(start)

    cnt = 0
    if grid[r][c] == 'G':
        cnt += 1
    if start in draft:
        return cnt
    else:
        for (rr, cc) in get4nb(r, c):
            if grid[rr][cc] != '#' and (rr, cc) not in visited:
                cnt += dfs((rr, cc), visited)
        return cnt

tot = dfs(start, set())
print(tot)