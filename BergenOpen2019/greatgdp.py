from __future__ import division

def nl():
    return [int(v) for v in raw_input().split()]
def ni():
    return int(raw_input())
def nl2():
    return [int(v)-1 for v in raw_input().split()]

def bfs(s, adj):
    q = [s]
    visited = set(q)
    layers = [-1] * len(adj)
    layers[s] = 0
    while q:
        q2 = []
        for a in q:
            for b in adj[a]:
                if b not in visited:
                    visited.add(b)
                    q2.append(b)
                    layers[b] = layers[a] + 1
        q = q2
    return layers

def test(av):
    DP = [0.0] * N
    mod_gdp = [gdp[i] - av*pop[i] for i in range(N)]
    for _, node in nodlay:
        v = mod_gdp[node]
        for b in adj[node]:
            v+= DP[b]
        DP[node] = max(v, 0.0)
    return DP[0] > 0.0


N = ni()
gdp = nl()
pop = nl()
adj = [[] for _ in range(N)]
for n in range(N-1):
    a, b = nl2()
    adj[a].append(b)
    adj[b].append(a)

layers = bfs(0, adj)
nodlay = [(lay, node) for node, lay in enumerate(layers)]
nodlay.sort(reverse= True)
hi = 10 **6
lo = 0.0
for t in range(50):
    mid = (lo + hi)/2.0
    ok = test(mid)
    if ok:
        lo = mid
    else:
        hi = mid
print(lo)
