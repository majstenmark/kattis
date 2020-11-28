import sys
from collections import deque
(col, row) = map(int, sys.stdin.readline().split())
g = []
for i in range(row):
    line = sys.stdin.readline().strip().split()
    sq = [int(c) for c in line]
    g.append(sq)

def obv_leaks(x, y, maxRows, maxCols):
    candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for (nx, ny) in candidates:
        if 0 <= nx < maxRows and 0 <= ny < maxCols:
            if g[nx][ny] < g[x][y]:
                return True
    return False

land = row * col
q = deque()

visited = set()

for r in range(row):
    for c in range(col):
        if obv_leaks(r, c, row, col):
            coord = (r, c)
            visited.add(coord)
            q.append(coord)


while q:
    (x, y) = q.popleft()
    candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for (nx, ny) in candidates:
        if 0 <= nx < row and 0 <= ny < col:
            if g[nx][ny] >= g[x][y] and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
land = land - len(visited)
print(land)
