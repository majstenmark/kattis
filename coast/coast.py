from collections import defaultdict as dd
from collections import deque

N, M = map(int, raw_input().split())
g = dd(int)
for i in range(N):
    line = raw_input()
    for j in range(M):
        g[i, j] = int(line[j])

visited = set()
q = deque()

for a in range(-1, N + 1):
    q.append((a, -1))
    q.append((a, M))
for b in range(-1, M + 1):
    q.append((-1, b))
    q.append((N, b))


coast = 0
while q:
    (x, y) = q.popleft()
    digit = g[x, y]
    neigh = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for (nx, ny) in neigh:
        if 0 <= nx < N and 0 <= ny < M:
            if g[nx, ny] == digit and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
            elif g[nx, ny] == 1:
                coast += 1

print(coast)
