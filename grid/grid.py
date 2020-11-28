import sys
from collections import deque
(n, m) = map(int, sys.stdin.readline().split())
g = []
for i in range(n):
    line = sys.stdin.readline().strip()
    chars = [int(c) for c in line]
    g.append(chars)
q = deque([(0, 0)])

visited = {(0, 0): 0}
found = False
dist = -1
while q and not found:
    (x, y) = q.popleft()


    digit = g[x][y]
    candidates = [(x + digit, y), (x - digit, y), (x, y + digit), (x, y - digit)]
    for (nx, ny) in candidates:
        if 0 <= nx < n and 0 <= ny < m:
            if (nx, ny) == (n-1, m-1):
                    #done
                dist = visited[(x, y)] + 1
                found = True
            if (nx, ny) not in visited:
                visited[(nx, ny)] = visited[(x, y)] + 1
                q.append((nx, ny))
print(dist)
