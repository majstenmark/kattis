from collections import defaultdict
from collections import defaultdict
class Dinitz:
    def __init__(self, sz, INF=10**10):
        self.G = [defaultdict(int) for _ in range(sz)]
        self.sz = sz
        self.INF = INF

    def add_edge(self, i, j, w):
        self.G[i][j] += w

    def bfs(self, s, t):
        level = [0]*self.sz
        q = [s]
        level[s] = 1
        while q:
            q2 = []
            for u in q:
                for v, w in self.G[u].items():
                    if w and level[v] == 0:
                        level[v] = level[u] + 1
                        q2.append(v)
            q = q2
        self.level = level
        return level[t] != 0

    def dfs(self, s, t, FLOW):
        if s in self.V: return 0
        if s == t: return FLOW
        self.V.add(s)
        L = self.level[s]
        for u, w in self.G[s].items():
            if u in self.dead: continue
            if w and L+1==self.level[u]:
                F = self.dfs(u, t, min(FLOW, w))
                if F:
                    self.G[s][u] -= F
                    self.G[u][s] += F
                    return F
        self.dead.add(s)
        return 0
    

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.dead = set()
            while True:
                self.V = set()    
                pushed = self.dfs(s, t, self.INF)
                if not pushed: break
                flow += pushed
        return flow

import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def nf(): return [float(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
em = [nf() for _ in range(N)]
ref = [nf() for _ in range(N)]

from math import sin, asin, cos, acos, pi, atan2
def angle(p, q):
    dy = p[1] - q[1]
    dx = p[0] - q[0]
    return 2 * abs(atan2(dx, dy))

ang = defaultdict(float) #ref to em
for i in range(N):
    for j in range(N):
        r = ref[i]
        e = em[j]
        a = angle(r, e)
        ang[i, j] = a

def test(a):
    F = Dinitz(2 * N + 2)
    for i in range(N):
        for j in range(N):
            #print(ang[i, j], a)
            if ang[i, j] <= a:
                F.add_edge(i, j + N, 1)
    S = 2 * N
    T = S + 1
    for i in range(N):
        F.add_edge(S, i, 1)
        F.add_edge(i + N, T, 1)
    mf = F.max_flow(S, T)
    #print(mf)
    return mf == N

lo = 0
hi = pi
for _ in range(40):
    mid = (hi + lo)/2
    if test(mid):
        hi = mid
    else:
        lo = mid
print(hi * 180/pi)