parents = []
def find(x):
    if parents[x][0] != x:
        parents[x][0] = find(parents[x][0])
    return parents[x][0]

def add(a_parent, b_parent):

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
        add(a_parent, b_parent)
    else:
        add(b_parent,a_parent)
    return True

N, M = map(int, raw_input().split())
while (N, M) != (0,0):
    edges = []
    for m  in range(M):
        u, v, w = map(int, raw_input().split())
        edges.append((w, u, v))
    parents = [[n, 1] for n in range(N)]
    edges.sort()
    treeWeight = 0
    treeEdges = []
    for w, u, v in edges:
        if union(u, v):
            treeWeight += w
            u, v = min(u, v), max(u, v)
            treeEdges.append((u, v))
    if len(treeEdges) != N - 1:
        print('Impossible')
    else:
        treeEdges.sort()
        print(treeWeight)
        for x, y in treeEdges:
            print('{} {}'.format(x, y))

    N, M = map(int, raw_input().split())
