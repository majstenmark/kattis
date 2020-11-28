import sys
itr = (line for line in sys.stdin.read().split('\n'))

def nl(): return [int(v) for v in next(itr).split()]
def ni(): return int(next(itr))


def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]

def vec(p1, p2):
    return p2[0]-p1[0], p2[1] - p1[1]

def sign(x):
    if x < 0: return -1
    return 1 if x > 0 else 0

def int_point(s, p):
    x = cross(vec(s[0], p), vec(*s))
    d = dot(vec(p, s[0]), vec(p, s[1]))
    return x == 0 and d < 0

def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]


def intersect(s1, s2):
    u = vec(*s1)
    v = vec(*s2)
    p1, p2 = s1
    q1, q2 = s2
    d1 = cross(u, vec(p1, q1))
    d2 = cross(u, vec(p1, q2))
    d3 = cross(v, vec(q1, p1))
    d4 = cross(v, vec(q1, p2))
    if d1 * d2 * d3 * d4 == 0:
        return False    
    return sign(d1) != sign(d2) and sign(d3) != sign(d4)

def fail():
    print(-1)
    exit()

def connectivity(g):
    q = [0]
    visited = set(q)
    
    while q:
        q2 = []
        for u in q:
            for ne in g[u]:
                if ne not in visited:
                    visited.add(ne)
                    q2.append(ne)
        q = q2
    return len(g)  == len(visited) 

N, M = nl()
if N == 1:
    print(1)
    exit()
dots = [tuple(nl()) for _ in range(N)]
seg = []

g = [[] for _ in range(N)]

points_with_segment = set()
for _ in range(M):
    i, j = nl()
    p1 = dots[i])
    p2 = dots[j]
    seg.append((p1, p2))

    points_with_segment.add(i)
    points_with_segment.add(j)
    g[i].append(j)
    g[j].append(i)

for i in range(N):
    if len(g[i]) == 0:
        fail()
    
if len(points_with_segment) != len(dots):
    fail()

if not connectivity(g):
    fail()

for i in range(M):
    s1 = seg[i]
    for j in range(i + 1, M):
        s2 = seg[j]
        if intersect(s1, s2):
            fail()
    for p in range(N):
        if int_point(s1, dots[p]):
            fail()  


print(len(seg) - len(dots) + 2)


