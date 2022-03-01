import sys
import math

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def nf(): 
    data =  inp().split()
    pos = [float(v) for v in data[0:-1]]
    ch = data[-1]
    return pos, ch

def ni(): return int(inp())

# Converts two points to a line (a, b, c), 
# ax + by + c = 0
# if p == q, a = b = c = 0 
def pts2line(p, q):
  return (-q[1] + p[1], 
          q[0] - p[0], 
          p[0]*q[1] - p[1]*q[0])

# Distance from a point to a line, 
# given that a != 0 or b != 0 
def distl(l, p):
  return (abs(l[0]*p[0] + l[1]*p[1] + l[2])
      /math.hypot(l[0], l[1]))

# projects a point on a line
def project(l, p):
  a, b, c = l
  return ((b*(b*p[0] - a*p[1]) - a*c)/(a*a + b*b), 
    (a*(a*p[1] - b*p[0]) - b*c)/(a*a + b*b))

def scal(u, v):
    return u[0]*v[0] + u[1]*v[1]

def sub(p, q):
    return (p[0] - q[0], p[1] - q[1])

def between(A, B, C):
    s1 = scal(sub(B, A), sub(C, A))
    s2 = scal(sub(A, B), sub(C, B))
    return s1*s2 >= 0

def getang(i, j):
    x1, y1, _, w, _ = habit[i]
    if abs(w) < 1e-8:
        return False, 0

    x2, y2, _, _, _ = habit[j]
    L = pts2line((x1, y1), (x2, y2))
    for k in range(H):
        if k != i and k != j:
            x3, y3, r, _, _ = habit[k]
            d = distl(L, (x3, y3))
            B = between((x1, y1), (x2, y2), (x3, y3))
            if B and d <= r:
                print(f'{i} and {j} has no straight line bc {k} is in the way!')
                return False, 0
    dy = y2 - y1
    dx = x2 - x1
    return True, math.atan2(dy, dx) % (2 * math.pi)

def getang2(i, j):
    x1, y1, _, _ , _ = habit[i]
    x2, y2, _, _, _ = habit[j]
    dy = y2 - y1
    dx = x2 - x1
    return True, math.atan2(dy, dx) % (2 * math.pi)

def dist(p, q):
  return math.hypot(p[0]-q[0], p[1] - q[1])


def calc_dist(i, j, time, theta):
    x1, y1, r1, w1, _ = habit[i]
    x2, y2, r2, _, _ = habit[j]

    travel = dist((x1, y1), (x2, y2)) -r1 -r2
    _, ang = getang2(i, j)
    da_l = (ang - theta) % (2 * math.pi)
    da_r = (2*math.pi - da_l)%(2*math.pi)
    if w1 < 0:
        angtime = da_r / abs(w1)
    else:
        angtime = da_l / abs(w1)

    travel_time = angtime + 2 * math.sqrt(2 * travel/acc)
    return time + travel_time, (ang + math.pi) % (2 * math.pi)

def calc_rot(i, ang_in, ang_out):
    w1 = habit[i][3]
    da_l = (ang_out - ang_in) % (2 * math.pi)
    da_r = (2*math.pi - da_l)%(2*math.pi)
    if w1 < 0:
        angtime = da_r / abs(w1)
    else:
        angtime = da_l / abs(w1)
    return angtime




line = inp().split()
H, Hstart = int(line[0]), int(line[1])
theta_start = float(line[2])
acc = float(line[3])
habit = []
for _ in range(H):
    li, ch = nf()
    x, y, r, om = li
    habit.append((x, y, r, om, ch))

e_id = 0
edgs = {}
g = [[] for _ in range(H)]
for i in range(H):
    for j in range(H):
        if i == j: continue
        ok, ang = getang(i, j)
        if ok:
            g[i].append((j, ang, e_id))
            edgs[e_id] = (i, j, ang, e_id)
            e_id += 1

#print(g)
import heapq

def dij(S, theta, g, rep):
    #g list with lists with tuples distance, other node
    # Dijkstra from S. Check t optionally
    INF = 10**12
    N = len(g)
    dist = [INF for _ in range(H)]

    pq = []
    for (nn, ang, e_id) in g[S]:
        t0 =  calc_rot(S, theta, ang)
        dist[e_id] = t0
        heapq.heappush(pq, (t0, e_id))

    done = False
    while pq and not done:
        _, e_id = heapq.heappop(pq)
        E = edgs[e_id]
        i, j, ang_in, _ = edgs[e_id]
        for (nn, ang_out, e_id) in g[j]:
            dd, theta2 = calc_dist(node, nn, nd, theta)
            alt = dist[node] + dd
            if dist[nn] > alt:
                dist[nn] = alt
                heapq.heappush(pq, (dist[nn], nn, theta2))

    return dist

print(g)

rep = set()
for node, (x, y, r, w, ch) in enumerate(habit):
    if ch == 't':
        rep.add(node)
mx = dij(Hstart, theta_start, g, rep)
print(mx)