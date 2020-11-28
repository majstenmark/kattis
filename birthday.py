import sys

itr = (int(line) for line in sys.stdin.read().split())
def g2():
    return next(itr), next(itr)

def connected(g, edge):
    q = [0]
    visited = set(q)
    while q:
        q2 = []
        for u in q:
            for v in g[u]:
                if (u, v) != edge and (v, u) != edge:
                    if v not in visited:
                        visited.add(v)
                        q2.append(v)
        q = q2
    return len(visited) == len(g)

def solve(p, c):
    edges = []
    g = [[] for _ in range(p)]
    for _ in range(c):
        a, b= g2()
        g[a].append(b)
        g[b].append(a)
        edges.append((a, b))
    for edge in edges:
        if not connected(g, edge):
            print('Yes')
            return
    print('No')

p, c = g2()
while p != 0:
    solve(p, c)
    p, c = g2()
    