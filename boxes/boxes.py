import sys

sys.setrecursionlimit(400000)

def dfs(this, children, count):
    if len(children[this]) == 0:
        count[this] = 1
        return 1
    if count[this] > 0:
        return count[this]
    c = 1
    for child in children[this]:
        c += dfs(child, children, count)
    count[this] = c
    return c

N= int(raw_input()) + 1
tree = map(int, raw_input().split())
children = [[] for n in range(N)]
count = [0 for n in range(N)]

for id, parent in enumerate(tree):
    children[parent].append(id + 1)

for i in range(N):
    if count[i] == 0:
        dfs(i, children, count)

P = [set() for n in range(N)]
Q = int(raw_input())
queries = []
for q in range(Q):
    Ms = map(int, raw_input().split())[1:]
    queries.append(Ms)
    for p1 in Ms[:-1]:
        for p2 in Ms[1:]:
            P[p1].add(p2)
            P[p2].add(p1)


parents = [[n, 1] for n in range(N)]
color = [0 for n in range(N)]
black = 1
def find(x):
    if parents[x][0] != x:
        parents[x][0] = find(parents[x][0])
    return parents[x][0]

def add(a, a_parent, b_parent):

    p,size= parents[b_parent]
    size += parents[a_parent][1]
    parents[b_parent] =  [b_parent, size]
    parents[a_parent][0] = b_parent

def union(a,b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent == b_parent:
        return False

    if parents[a_parent][1] < parents[b_parent][1]:
        add(a,a_parent, b_parent)
    else:
        add(b, b_parent,a_parent)
    return True
lca = {}

def LCA(u):
    for v in children[u]:
        LCA(v);
        union(u,v);
        uR = find(u)
        parents[uR][0] = u
        parents[u][0] = u
    color[u] = black
    for v in P[u]:
        if color[v] == black:
            lca[u,v] = parents[find(v)][0]
            lca[v, u] = lca[u,v]


LCA(0)

for query in queries:
    #print(q)
    q =list(set(query))
    use = [True for _ in range(len(q))]
    for index in range(len(q) -1):
        for index2 in range(index+1, len(q)):
            parent = lca[q[index], q[index2]]
            if parent == q[index]:
                use[index2] = False
            if parent == q[index2]:
                use[index] = False
    size = 0
    for index in range(len(q)):
        if use[index]:
            size +=  count[q[index]]
    print(size)
