import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())


def bfs(q, grid, visited, R, C):
    for node in q:
        visited.add(node)
    while q:
        q2 = []
        for r, c in q:
            cand = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dr, dc in cand:
                if 0<= r + dr < R and 0 <= c + dc < C:
                    rr, cc = r + dr, c + dc
                    if grid[rr][cc] == '-':
                        ne = rr, cc
                        if ne not in visited:
                            visited.add(ne)
                            q2.append(ne)
        q = q2
    return visited

def solve(R, C, grid):
    cnt = 0
    visited = set()
    for m in range(M):
        for n in range(N):
            if grid[m][n] == '-' and (m, n) not in visited:
                cnt += 1
                bfs([(m, n)], grid, visited, R, C)
    return cnt

cnt = 1
while True:
    indata = next(itr, "")
    if indata == "":
        break
    M, N = [int(v) for v in indata.split()]

    grid = [inp() for _ in range(M)]
    sol = solve(M, N, grid)
    print(f'Case {cnt}: {sol}')
    cnt += 1
