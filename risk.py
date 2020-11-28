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

        
import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)

def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())


def test(N, g, enemies, border, innerNodes, armies, bottleneck):

    #every node gets an out node with id 2 * id.
    S = 2* N
    T = S + 1
    f = Flow(2 * N + 2)
    #print('bottleneck', bottleneck)
    

    for node in range(N):
        if node not in enemies:
            cap = armies[node]
            out = N +  node

            f.add_edge(S, node, cap)
            f.add_edge(node, out, cap)
            #print('node', node, 'g list', g[node])
            for ne in g[node]:
                if ne not in enemies:
                    ne_out = N + ne
                    f.add_edge(node, ne_out, cap)
            if node in border:
                f.add_edge(out, T, bottleneck)
            else:
                f.add_edge(out, T, 1)


    maxF = f.max_flow(S, T)
    #print('maxf', maxF)
    if maxF == innerNodes + len(border) * bottleneck:
        #print(f.G)
        return True
    return False
    


tests = ni()
for _ in range(tests):
    N = ni()
    armies = nl()
    adj = []
    g = [[] for _ in range(N)]
    for r in range(N):
        a = inp()
        for c, ch in enumerate(a):
            if ch == 'Y':
                g[r].append(c)
    #find the enemy nodes
    enemies = set()
    for i, no in enumerate(armies):
        if no == 0:
            enemies.add(i)
    border = set()
    for enemy in enemies:
        for ne in g[enemy]:
            if ne not in enemies:
                border.add(ne)
    innerNodes = 0
    for node in range(N):
        if node not in border and node not in enemies:
            innerNodes += 1
    #print('Innernodes', innerNodes)
    lo, hi = 1, 10001
    while lo < hi-1:
        mid = (lo + hi)//2
        res =  test(N, g, enemies, border, innerNodes, armies, mid)
        if res:
            lo = mid
        else:
            hi = mid
    print(lo)