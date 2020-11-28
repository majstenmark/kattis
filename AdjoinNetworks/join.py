C, L = map(int, raw_input().split())
g = [[] for _ in range(C)]
for l in range(L):
    u, v  = map(int, raw_input().split())
    g[u].append(v)
    g[v].append(u)

forward = [False] * C
backward = [False] * C

def bfs(node, g, visited):
    q   = [node]
    visited[node] = True
    layers = -1
    while q:
        layers += 1
        q2 = []
        for node in q:
            for ne in g[node]:
                if not visited[ne]:
                    visited[ne] = True
                    q2.append(ne)

        q = q2
    return node, layers

diams = []
for c in range(C):
    if not forward[c]:
        endpoint, _ = bfs(c, g, forward)
        _, diam = bfs(endpoint, g, backward)
        #print 'diam ', diam, ' radius', (diam + 1)/2
        diams.append(diam)

if len(diams) == 1:
    print(diams[0])
elif len(diams) == 2:

    v = max((diams[0] + 1)/2 + (diams[1] + 1)/2 + 1, max(diams))
    print v
else:
    largest = 0
    second_largest = 0
    third_largest = 0
    for d in diams:
        if d > largest:
            largest, second_largest, third_largest = d, largest, second_largest
        elif d > second_largest:
            second_largest, third_largest = d, second_largest
        elif d > third_largest:
            third_largest = d
    r1 = (largest + 1)/2
    r2 = (second_largest + 1)/2
    r3 = (third_largest + 1)/2
    v = max(r1 + r2 + 1, largest, r2+ r3 + 2)
    print v
