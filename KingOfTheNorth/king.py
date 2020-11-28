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

R, C = map(int, raw_input().split())
N = 2 * R * C + 1
L2 = R * C
kingdom = [[(0,0)] * C for _ in range(R)]
id = 0
for r in range(R):
    tiles = map(int, raw_input().split())
    for c in range(C):
        kingdom[r][c] = (tiles[c], id)
        id += 1
sinkId = N - 1
#print(kingdom)
castleR, castleC = map(int, raw_input().split())
cmen, cid = kingdom[castleR][castleC]
# build graph
flow = Flow(N)

INF = 10**12
for r in range(R):
    for c in range(C):
        men, id = kingdom[r][c]
        neigbors = [(r + 1, c),(r - 1, c), (r, c + 1), (r , c - 1)]
        for cr, cc in neigbors:
            if cr < 0 or cr == R or cc < 0 or cc == C:
                # on the edge
                flow.add_edge(sinkId, id, INF)
                flow.add_edge(id + L2, sinkId, INF)
            else:
                nmen, nid = kingdom[cr][cc]
                flow.add_edge(nid + L2, id, INF)
                flow.add_edge(id + L2, nid, INF)

            flow.add_edge(id, id + L2, men)
#print(flow.p())
mf = flow.max_flow(cid, sinkId)
print(mf)
