from collections import deque

n = int(raw_input())
g = [[] for _ in range(n)]
q = []

visited = [[-1 for x in range(n)] for _ in range(n)]

for i in range(n):
    line = raw_input()
    for j in range(n):
        g[i].append(int(line[j]))
        if g[i][j] == 3:
            q.append((i, j))
            visited[i][j] = 0

while q:
    q2 = []
    for (x, y) in q:
        candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for (nx, ny) in candidates:
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q2.append((nx, ny))
    q = q2

dist = 0
for x in range(n):
    for y in range(n):
        if g[x][y] == 1:
            dist = max(dist, visited[x][y])
print(dist)
