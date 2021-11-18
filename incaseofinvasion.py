import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

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


import heapq

def dij(S, g):
    #g list with lists with tuples distance, other node
    # Dijkstra from S. Check t optionally
    INF = 10**40
    N = len(g)
    dist = [INF for _ in range(N)]

    pq = []
    dist[S] = 0
    pq.append((0, S))
    heapq.heapify(pq)
    done = False
    while pq and not done:
        (nd, node) = heapq.heappop(pq)
        #if node == T: return dist[T]
        for (dd, nn) in g[node]:
            alt = dist[node] + dd
            if dist[nn] > alt:
                dist[nn] = alt
                heapq.heappush(pq, (dist[nn], nn))

    return dist


def test(mx, shelters, sh_dists, scaps, ppl, tot):
    K = N + 2 + len(shelters)
    net = Dinitz(K)
    source = K - 2
    T = K -1

    for n in range(N):
        net.add_edge(source, n, ppl[n])
    for index, s in enumerate(shelters):
        sid = index + N
        net.add_edge(sid, T, scaps[s])

        for n in range(N):
            if sh_dists[s][n] <= mx:
                net.add_edge(n, sid, ppl[n])
    f = net.max_flow(source, T)
    return f >= tot


N, M, S = nl()
ppl = nl()
tot = sum(ppl)
edges = [nl() for _ in range(M)]
shelters = set()
scap = {}
for _ in range(S):
    s, c = nl()
    shelters.add(s-1)
    scap[s-1] = c

G = [[] for _ in range(N)]
for u, v, c in edges:
    G[u-1].append((c, v-1))
    G[v-1].append((c, u-1))
sh_dists = {}
for s in shelters:
    dist = dij(s, G)
    sh_dists[s] = dist
 
mx = 0
for li in sh_dists.values():
    mx = max(mx, max(li))

hi = mx + 1
lo = 0
while lo < hi:
    mid = (lo + hi)//2
    #print('Testing ', mid, lo, hi)
    res = test(mid, shelters, sh_dists, scap, ppl, tot)
    #print(res)
    if res:
        hi = mid
    else:
        lo = mid + 1
print(hi)

