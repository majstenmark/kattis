N, M = map(int, raw_input().split())
name2int = {}
isAs = []
hasAs = []
for line in range(N):
    As, rel, Bs = raw_input().split()
    A, B = 0, 0
    if not As in name2int:
        name2int[As] = len(name2int)
    if not Bs in name2int:
        name2int[Bs] = len(name2int)
    A = name2int[As]
    B = name2int[Bs]
    if rel == "is-a":
        isAs.append((A, B))
    else:
        hasAs.append((A, B))

sz = len(name2int)

sup = [set() for _ in range(sz)]
sub  = [set() for _ in range(sz)]
hasA = [set() for _ in range(sz)]
g = [[] for _ in range(sz)]
G2= [[] for _ in range(sz)]
hasA2 = [set() for _ in range(sz)]


for a, b in isAs:
    g[a].append(b)
    G2[a].append(b)

for a, b in hasAs:
    G2[a].append(b)



def bfs(q, g):
    visited = set()
    for v in q:
        visited.add(v)
    while q:
        q2 = []
        for node in q:
            for ne in g[node]:
                if ne not in visited:
                    visited.add(ne)
                    q2.append(ne)
        q = q2
    return visited

for n in range(sz):
    supers = bfs([n], g)
    sup[n] = supers
    for s in supers:
        sub[s].add(n)

for a, b in hasAs:
    for subclass in sub[a]:
        hasA[subclass].add(b)

for i in range(sz):
    hasA2[i] = bfs(list(hasA[i]), G2)

def ans(A, B, rel):
    if rel == "has-a":
        return B in hasA2[A]
    else:
        return B in sup[A]

for q in range(M):
    As, rel, Bs = raw_input().split()
    A = name2int[As]
    B = name2int[Bs]
    res = ans(A, B, rel)
    if res:
        print "Query {}: true".format(q+1)
    else:
        print "Query {}: false".format(q+1)
