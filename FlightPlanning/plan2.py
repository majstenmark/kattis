from collections import Counter
from collections import deque


def getDiam(tree):

    lastnode1, _, _ = bfs(0, tree)
    _, dist, _ = bfs(lastnode1, tree)
    return dist -1;



def bfs(f, g):
    visited = set()
    layers = 0
    q = [f]
    visited.add(f)
    while q:
        q2 = []
        for node in q:
            for ne in g[node]:
                if ne not in visited:
                    visited.add(ne)

                    q2.append(ne)
        q = q2
        layers +=1
    return node, layers, visited


def cent(T, intree):
    qu = deque([])
    cnt = Counter()

    for n in intree:
        cnt[n] = len(T[n])
        if len(T[n]) <= 1:
            qu.append(n)
#    print 'intree', intree
    last = n
    leaf = n
    used = set(qu)
    while qu:
        last = leaf

        leaf = qu.popleft()
        for ne in T[leaf]:
            cnt[ne] -= 1
            if cnt[ne] <= 1 and ne not in used:
                used.add(ne)
                qu.append(ne)
    return [leaf, last]

def testToRemove(midnode, tree):
    #depth = calcDepth(midnode, tree)
    MIN = 10 ** 12
    add = []
    canc = []
    #print 'for midnode', midnode
    for ne in list(tree[midnode]):
        tree[ne].remove(midnode)
        tree[midnode].remove(ne)
        _, _, inleft = bfs(ne, tree)
        _, _, inright = bfs(midnode, tree)
        leftnode = cent(tree, inleft)[0]
        rightnode = cent(tree, inright)[0]

        tree[rightnode].append(leftnode)
        tree[leftnode].append(rightnode)
        diam = getDiam(tree)
        if diam < MIN:
            MIN = diam
            canc = [ne, midnode]
            add = [leftnode, rightnode]

        tree[rightnode].remove(leftnode)
        tree[leftnode].remove(rightnode)


        tree[ne].append(midnode)
        tree[midnode].append(ne)
    return MIN, canc, add


N = input()
tree = [[] for _ in range(N)]
for n in range(N-1):
    a, b = map(int, raw_input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

MIN = 10 **12
canc = []
all = set([n for n in range(N)])
mids = cent(tree, all)
for midnode in mids:
    d, c, a = testToRemove(midnode, tree)
    #print d, c, a
    if d < MIN:
        MIN = d
        canc = c
        add = a

print MIN
print str(canc[0] +1) + ' ' + str(canc[1] +1)
print str(add[0] +1) + ' ' + str(add[1] +1)
