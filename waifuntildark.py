from collections import defaultdict 
class Flow:
    def __init__(self, sz):
        self.G = [defaultdict(int) for _ in range(sz)]
    
    def add_edge(self, i, j, w):
        self.G[i][j] = w
    
    def bfs(self, s, t):
        vis = {s:s}
        q = [s]
        while q:
            q2 = []
            for u in q:
                for v, w in self.G[u].items():
                    if w and not v in vis:
                        vis[v] = u
                        q2.append(v)
                        if v == t:
                            return self.reconstruct(s, t, vis)
            q = q2
        return 0

    def reconstruct(self, s, t, vis):
        path = [t]
        push = 10**18
        while t != s:
            push = min(push, self.G[vis[t]][t])
            t = vis[t]
            path.append(t)
        for i in range(len(path) - 1):
            self.G[path[i+1]][path[i]] -= push
            self.G[path[i]][path[i+1]] += push
        return push

    def max_flow(self, s, t):
        flow = 0
        while True:
            pushed = self.bfs(s, t)
            if not pushed: break
            flow += pushed
        return flow


N, M, P = [int(v) for v in raw_input().split()]
S = 0
T = N + M + P +1 #id
F = Flow(T+1)
for n in range(N):
    toys = [int(v) for v in raw_input().split()][1:]
    child = n+1
    F.add_edge(S, child, 1)
    for toy in toys:
        F.add_edge(child, toy + N, 1)

usedtoys = set()
for p in range(P):
    data = [int(v) for v in raw_input().split()]
    r = data[-1]
    cat= data[1:-1]
    catid = p + 1+ N + M
    for toy in cat:
        usedtoys.add(toy)
        toyid = toy + N
        F.add_edge(toyid, catid, 1)
    F.add_edge(catid, T, r)
for toy in range(1,M+1):
    if toy not in usedtoys:
        F.add_edge(toy + N, T, 1)
#print(F.G)
mx= F.max_flow(S, T)
print(mx)
    
    