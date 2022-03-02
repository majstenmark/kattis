import sys
from collections import defaultdict as dd
itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

INF = 10**12
def id(x,y, w):
    return x + y * w

def bfs(q, w, h):
    N = w * h
    dists = [INF] * N
    for x,y in q:
        dists[id(x, y, w)] = 0
    
    while q:
        q2 = []
        for x, y in q:
            alt = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for xx, yy in alt:
                if 0 <= xx < w and 0 <= yy < h:
                    idx = id(xx, yy, w)
                    if dists[idx] == INF:
                        dists[idx] = dists[id(x, y, w)] + 1
                        q2.append((xx, yy))
        q = q2
    return dists

def dist(l, r):
    dx = abs(l[0] - r[0])
    dy = abs(l[1] - r[1])
    return dx + dy
    

def test(dists, w, h, M):
    left = []
    right = []
    for y in range(h):
        l = None
        r = None
        for x in range(w):
            if dists[id(x, y, w)] >= M:
                if l == None:
                    l = x, y
                r = x, y
        if l != None: left.append(l)
        if r != None: right.append(r)
    for l in left:
        for r in right:
            if dist(l, r) >= M:
                return True
    return False


def find(dists, w, h):
    lo = 0
    hi = w + h + 1
    for i in range(11):
        mid = (lo + hi+ 1)//2
        #print(mid, lo, hi)
        if test(dists, w, h, mid):
            lo = mid
        else:
            hi = mid
    return lo
    

T = ni()
out = []
for _ in range(T):
    n, w, h = nl()
    if n > 0:
        stands = [tuple(nl()) for _ in range(n)]
        dists = bfs(stands, w, h)
        res = find(dists, w, h)
        out.append(str(res))
    else:
        out.append(str(w + h -2))
print('\n'.join(out))
