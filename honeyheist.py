from collections import defaultdict as dd

inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def add(id):
    if id in hard:
        return
    pos = [(-1, -1), (-1,1),(1,-1),(1, 1), (0,-2), (0, 2)]
    row,col = ids[id]
    for dr, dc in pos:
        r = row + dr
        c = col + dc
        if 0<= r < len(grid) and 0<= c < len(grid[r]) and grid[r][c] != None and grid[r][c] not in hard:
            g[id].append(grid[r][c])

def printgrid(grid, path):
    p = set(path)
    for row in range(len(grid)):
        out = []
        for c in grid[row]:
            if c == None:
                out.append('.')
            elif c in hard:
                out.append('xxx')
            elif c in p:
                out.append('###')
            else:
                
                s = str(c)
                s = '0' * (3 -len(s)) + s
                out.append(s)
        print(''.join(out))

R, N, A, B, X = nl()
hard = set(nl())
tot = (R ** 3 - (R-1) **3)
g = dd(list)
grid = [[] for _ in range(2 * R -1)]
row = 0
totRow = R + (R -1) * 3
for cnt in range(R-1, 0, -1):
    for empty in range(cnt):
        grid[row].append(None)
    row += 1
row = R
for cnt in range(1, R):
    for empty in range(cnt):
        grid[row].append(None)
    row += 1
id = 1
for row in range(R):
    for c in range(row + R):
        grid[row].append(id)
        grid[row].append(None)
        id += 1
    while len(grid[row]) < totRow:
        grid[row].append(None)

for row in range(R-1):
    tmpRow = row + R
    for c in range(2 * R -2 - row):
        grid[tmpRow].append(id)
        grid[tmpRow].append(None)
        id += 1
    while len(grid[tmpRow]) < totRow:
        grid[tmpRow].append(None)
ids = {}
coords = {}
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] != None:
            ids[grid[row][col]] = (row,col)
            coords[row, col] = grid[row][col]
for id in ids.keys():
    add(id)

def bfs(q, g):
    visited = set(q)
    dist = 0
    path = {}
    while q:
        q2 = []
        for node in q:
            if node == B:
                p = []
                parent = path[B]
                while parent in path:
                    p.append(parent)
                    parent = path[parent]
                return dist, p
            for ne in g[node]:
                if ne not in visited:
                    visited.add(ne)
                    q2.append(ne)
                    path[ne] = node
        q = q2
        dist += 1
    return 10 ** 12, []

k, path = bfs([A], g)
#printgrid(grid, path)
#print('tot', tot, g[91])
#print(path, k)
#print(g)
if k <= N:
    print(k)
else:
    print('No')