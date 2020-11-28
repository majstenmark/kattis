def dist_w(p, q):
    return ((p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2)**.5

N, M = map(int, raw_input().split())
INF = 10**18
dist = [[INF]*N for _ in range(N)]
nxt = [[None]*N for _ in range(N)]
pts = []
for _ in range(N):
    f, x, y = map(int, raw_input().split())
    pts.append((x, y, f*5))

edgs = []
for _ in range(M):
    a, b, c = raw_input().split()
    a, b = int(a), int(b)
    if c == 'walking' or c == 'stairs':
        d = dist_w(pts[a], pts[b])
        edgs.append((a, b, d))
        edgs.append((b, a, d))
    elif c == 'lift':
        edgs.append((a, b, 1))
        edgs.append((b, a, 1))
    elif c == 'escalator':
        edgs.append((a, b, 1))
        edgs.append((b, a, dist_w(pts[a], pts[b])*3))
    else:
        assert 0

for i in range(N):
    nxt[i][i] = i

for i, j, c in edgs:
    if c < dist[i][j]:
        dist[i][j] = c
        nxt[i][j] = j

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                nxt[i][j] = nxt[i][k]

def path(i, j):
    if nxt[i][j] == None:
        assert 0
        return []
    p = [i]
    while i != j:
        i = nxt[i][j]
        p.append(i)
    return p

Q = input()
for _ in range(Q):
    a, b = map(int, raw_input().split())
    p = path(a, b)
    print(' '.join(map(str, p)))
