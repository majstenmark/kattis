from collections import *
import sys
sys.setrecursionlimit(10000)
inp = input
def ni(): return int(inp())
def nl(): return [int(v) for v in inp().split()]

def getFirst(G, R, C):
    for i in range(R):
        for j in range(C):
            if G[i][j]:
                return (i, j)

def test(si, sj, L):
    for i in range(si, si+L):
        for j in range(sj, sj+L):
            if not G_O[i][j]:
                return False
    return True

def getAll(G, R, C):
    o = []
    for i in range(R):
        for j in range(C):
            if G[i][j]:
                o.append((i, j))
    return o

R, C = nl()
G = [[ch == 'x' for ch in inp()] for _ in range(R)]
G_O = [list(l) for l in G]
si, sj = getFirst(G, R, C)
L = 1
while True:
    t = L + 1
    if si + t > R or sj + t > C:
        break
    ok = True
    for i in range(si, si + t):
        if not G[i][sj+L]:
            ok = False
    for j in range(sj, sj+t):
        if not G[si+L][j]:
            ok = False
    if not ok: break
    L = t
for i in range(si, si+L):
    for j in range(sj, sj+L):
        G[i][j] = False
print(si+1, sj+1, L)
A = getAll(G, R, C)
if not A:
    print(si+1, sj+1, L)
else:
    MAXx, MAXy = max(A)
    MINx, MINy = MAXx, MAXy
    for x, y in A:
        MINx = min(MINx, x)
        MINy = min(MINy, y)
    dx = MAXx - MINx
    dy = MAXy - MINy
    dd = max(dx, dy)
    ox, oy = MAXx - dd, MAXy - dd
    if test(ox, oy, dd+1):
        print(ox + 1, oy + 1, dd + 1)
    else:
        assert test(MINx, MINy, dd+1)
        print(MINx+1, MINy+1, dd+1)

