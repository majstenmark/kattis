

def id(x, y):
    return y * X + x

def find(x):
    y = p[x]
    while y != x:
        p[x] = p[y]
        x, y = y, p[y]
    return p[x]


def union(a,b):
    ap = find(a)
    bp = find(b)
    if ap == bp:
        return False

    if s[ap] < s[bp]:
        s[bp] +=  s[ap]
        p[ap] = bp
    else:
        s[ap] +=  s[bp]
        p[bp] = ap
    return True

def flood(x0, y0):
    oId = id(x0, y0)
    q = [(x0, y0)]
    p[oId] = oId
    c = 1
    while q:
        q2 = []
        for x, y in q:
            nes = [(x + 1, y), (x -1, y), (x, y + 1), (x, y -1)]
            for neX, neY in nes:
                if 0 <= neX < X and 0 <= neY < Y and grid[neX][neY] == WHITE and p[id(neX, neY)] == -1:
                    q2.append((neX, neY))
                    p[id(neX,neY)] =oId
                    c += 1
        q = q2
    s[oId] = c

X, Y, Q = map(int, raw_input().split())
strokes = []
WHITE = 0
BLACK = 1
grid = [[WHITE] * Y for x in range(X)]
strokes = [[] for _ in range(Q)]
nbrOfRegions = 0
p = [-1 for x in range(X*Y)]
s = [1 for x in range(X*Y)]

for q in xrange(Q):
    x1, y1, x2, y2 = map(int, raw_input().split())
    for x in xrange(x1 - 1, x2, 1):
        for y in xrange(y1-1, y2, 1):
            if grid[x][y] == WHITE:
                grid[x][y] = BLACK
                strokes[q].append((x, y))
#                   sprint grid
for x in xrange(X):
    for y in xrange(Y):
        if grid[x][y] == WHITE and p[id(x, y)] == -1:
            nbrOfRegions += 1
            flood(x, y)

regions = ['0' for _ in xrange(Q)]
regions[Q-1] = str(nbrOfRegions)
for q in xrange(Q - 1, 0, -1):
    for x, y in strokes[q]:
        i =id(x,y)
        p[i] = i
        s[i] = 1
        grid[x][y] = WHITE
        nbrOfRegions += 1
        nes = [(x + 1, y), (x -1, y), (x, y + 1), (x, y -1)]
        for neX, neY in nes:
            if 0 <= neX < X and 0 <= neY < Y and grid[neX][neY] == WHITE:
                if union(i, id(neX, neY)):
                    nbrOfRegions -= 1
    regions[q -1] = str(nbrOfRegions)
s  = '\n'.join(regions)
print s
