def cent(fromnode, dist, parents,tree):
    centroids = []
    curr = fromnode
    for step in range((dist-1)/2):
        curr = parents[curr]
    centroids.append(curr)
    if dist % 2 == 0:
        centroids.append(parents[curr])
    depth1 = calcDepth(centroids[0], tree)
    maxD1 = depth1[centroids[0]]

    res = [(centroids[0], depth1, maxD1)]

    if len(centroids) == 2:
        depth2 = calcDepth(centroids[1], tree)
        maxD2 = depth2[centroids[1]]

        res.append((centroids[1], depth2, maxD2))

    return res

def calcDepth(fromNode, tree):
    q = [fromNode]

    visited = [False] * N
    visited[fromNode] = True
    stack = []
    while q:
        q2 = []
        for node in q:
            stack.append(node)
            for ne in tree[node]:

                if not visited[ne]:
                    visited[ne] = True
                    q2.append(ne)
        q = q2
    depth = [-1] * N
    #print 'stack', stack[::-1]
    for node in stack[::-1]:
        MAXD = 0
        for ne in tree[node]:
            MAXD = max(depth[ne] +1, MAXD)
        depth[node] = MAXD
    return depth


def rebuild(c, tree, depth):
    maxD = 0
    subtrees = []
    for ne in tree[c]:
        subtrees.append((depth[ne], ne))
    subtrees.sort(reverse = True)
    maxDiam = 10 ** 12
    bestCanceled = ()
    bestadded = ()
    for _, subtree in subtrees[0:3]:
        canceled = (c, subtree)
        tree[c].remove(subtree)
        tree[subtree].remove(c)
    #    print 'canceled', canceled
        candidates1 = getCentroid(subtrees[0][1], tree)
        candidates2 = getCentroid(subtrees[1][1], tree)

        for c1, d1, maxD1 in candidates1:
            for c2, d2, maxD2 in candidates2:
                if maxD1 + maxD2 + 1 < maxDiam:
                #    print 'd1', d1,'max', maxD1
                #    print 'd2', d2,'max', maxD2
                    bestCanceled = canceled
                    maxDiam = maxD1 + maxD2 + 1
                    bestadded = (c1, c2)

        tree[c].append(subtree)
        tree[subtree].append(c)

    return bestCanceled, bestadded, maxDiam

def getCentroid(anynode, tree):

    firstend, _, _ = bfs([anynode], tree)
    secondend, dist, parents = bfs([firstend], tree)
    return cent(secondend, dist,parents,tree)


def bfs(q, g):
    visited = [False] * N
    layers = 0
    parents = [-1 for _ in range(N)]
    for node in q:
        visited[node] = True
    lastnode = node
    while q:
        q2 = []
        for node in q:
            for ne in g[node]:
                if not visited[ne]:
                    visited[ne] = True
                    lastnode = ne
                    parents[ne] = node
                    q2.append(ne)
        q = q2
        layers +=1
    return lastnode, layers, parents

N = input()
tree = [[] for _ in range(N)]
for n in range(N-1):
    a, b = map(int, raw_input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
#print "calc depth"
candidates = getCentroid(0, tree)
MAX = 10 **12
canc = ()
add = ()
for centCand, depthCand, maxDCand in candidates:
    _canc, _add, maxD = rebuild(centCand, tree, depthCand)
    if maxD < MAX:
    #    print _canc, _add, maxD, MAX

        canc = _canc
        add= _add
        MAX = maxD

print MAX
print str(canc[0] +1) + ' ' + str(canc[1] +1)
print str(add[0] +1) + ' ' + str(add[1] +1)
