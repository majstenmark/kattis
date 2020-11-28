from collections import deque

A, F = map(int, raw_input().split())
L,V = map(int, raw_input().split())
whites = []
A2 = A **2

for y in range(L):
    line = raw_input()
    for x in range(len(line)):
        if line[x] == 'S':
            start = len(whites)
        if line[x] == 'G':
            goal = len(whites)
        if line[x] != 'B':
            whites.append((len(whites), x, y))

def closeBy(a, b, maxStep2):
    dX = a[1] - b[1]
    dY = a[2] - b[2]
    return dX**2 + dY**2 <= maxStep2

def closeByXY(a, b, maxStep):
    dX = abs(a[1] - b[1])
    dY = abs(a[2] - b[2])
    return dX == 0 and dY <= maxStep or dY == 0 and dX <= maxStep


gElise = [[] for _ in range(len(whites))]
gFather = [[] for _ in range(len(whites))]
for w in whites:
    for other in whites:
        if w == other: continue
        if closeBy(w, other, A2):
            gElise[w[0]].append(other[0])
        if closeByXY(w, other, F):
            gFather[w[0]].append(other[0])

# bfs
def bfs(g):
    q = deque([start])
    visited = {start:0}
    while q:
        tmp = q.popleft()
        if tmp == goal:
            return visited[tmp]
        for n in g[tmp]:
            if n not in visited:
                visited[n] = visited[tmp] + 1
                q.append(n)
    return 1000000

eRes = bfs(gElise)
fRes = bfs(gFather)
#print('eres', eRes, 'fres',fRes)
if eRes == fRes == 1000000:
    print('NO WAY')
elif eRes == fRes:
    print('SUCCESS')
elif eRes < fRes:
    print('GO FOR IT')
else:
    print('NO CHANCE')
