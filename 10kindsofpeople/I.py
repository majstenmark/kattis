import sys
from collections import deque
r, c = map(int, raw_input().split())
g = []
for i in range(r):
    line = raw_input()
    sq = [int(ch) for ch in line]
    g.append(sq)


areas = {}
def flood(a, b, grid, areas):
    q = deque([(a, b)])
    areas[a, b]  = len(areas)
    while q:
        (x, y) = q.popleft()

        digit = grid[x][y]

        neigh = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for (nx, ny) in neigh:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == digit and (nx, ny) not in areas:
                    areas[nx, ny] = areas[a, b]
                    q.append((nx, ny))

for a in range(r):
    for b in range(c):
        if (a,b) not in areas:
            flood(a, b, g, areas)

n = int(raw_input())
for i in range(n):
    (r1, c1, r2, c2) = map(lambda x: int(x) -1, raw_input().split())

    if areas[r1, c1] == areas[r2, c2]:

        if g[r1][c1] == 0:
            print "binary"
        else:
            print "decimal"
    else:
        print "neither"
