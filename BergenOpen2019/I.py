from collections import defaultdict
class Flow:
    def __init__(self, sz):
        self.G = [defaultdict(int) for _ in range(sz)]
    
    def add_edge(self, i, j, w):
        self.G[i][j] += w
    
    def dfs(self, s, t, FLOW):
        if s in self.V: return 0
        if s == t: return FLOW
        self.V.add(s)
        for u, w in self.G[s].items():
            if w:
                F = self.dfs(u, t, min(FLOW, w))
                if F:
                    self.G[s][u] -= F
                    self.G[u][s] += F
                    return F
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.V = set()
            pushed = self.dfs(s, t, 1)
            if not pushed: break
            flow += pushed
        return flow

def nl():
    return [int(v) for v in raw_input().split()]

def ni():
    return int(raw_input())

N, M = nl()
F, C, V = nl()
sz = N + 1
net = Flow(sz)
for m in range(M):
    u, v, x = nl()
    net.add_edge(u, v, 2*x)
    net.add_edge(v, u, 2*x)
T = F
c = 0
while True:
    net.add_edge(0, C, 1)
    net.add_edge(0, V, 1)
    if net.max_flow(0, T) != 2:
        print(c)
        exit()
    c += 1


    
