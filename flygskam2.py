import sys
import math

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())
def pos():
    data = inp().split()
    return data[0], float(data[1]), float(data[2])

R = 6381
R2 = R * R

N, M = nl()
S, T = inp().split()
#vectors = [0] * N
positions = [0] * N

def torad(deg):
    return deg/180.0 * math.pi

def vec(latdeg, longdeg):
    lat = torad(latdeg)
    long = torad(longdeg)

    z = math.sin(lat) * R
    Rtmp = math.cos(lat) * R
    x = math.cos(long) * Rtmp
    y = math.sin(long) * Rtmp
    return x, y, z


def angle(v1, v2):
    dot = v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
    
    val = dot/R2
    
    return math.acos(val)



def dist(a, b):
    #avec = vectors[a]
    #bvec = vectors[b]
    #alpha = angle(avec, bvec)
    theta1, lambda1 = positions[a]
    theta2, lambda2 = positions[b]
    sintheta1 = math.sin(theta1)
    sintheta2 = math.sin(theta2)
    costheta1 = math.cos(theta1)
    costheta2 = math.cos(theta2)
    deltalambda = abs(lambda2 - lambda1)
    sindelta = math.sin(deltalambda)
    cosdelta = math.cos(deltalambda)
    A = math.pow(costheta2 * sindelta, 2)
    B = math.pow(costheta1 * sintheta2 - sintheta1 * costheta2 * cosdelta, 2)
    C = math.sqrt(A + B)
    D = sintheta1 * sintheta2 + costheta1 * costheta2 * cosdelta
    
    alpha = math.atan2(C,D)
    
    
    arc = R * alpha
    return 100 + arc


seen = {}

def init(a):
    if a not in seen:
        ida = len(seen)
        seen[a] = ida
    return seen[a]


for _ in range(N):
    name, lat, long = pos()
    id = init(name)
    #vectors[id] = vec(lat, long)
    positions[id] = (torad(lat), torad(long))

g = [[] for _ in range(N)]
for _ in range(M):
    a, b = inp().split()
    ida = seen[a]
    idb = seen[b]
    d = dist(ida, idb)
    
    g[ida].append((d, idb))
    g[idb].append((d, ida))

    
import heapq

def dij(S, T, g):
    #g list with lists with tuples distance, other node
    # Dijkstra from S. Check t optionally
    INF = 10**12
   
    dist = [INF for _ in range(N)]
    pq = []
    dist[S] = 0
    pq.append((0, S))
    heapq.heapify(pq)
    while pq:
        (nd, node) = heapq.heappop(pq)
        if node == T: return dist[T]
        for (dd, nn) in g[node]:
            alt = dist[node] + dd
            if dist[nn] > alt:
                dist[nn] = alt
                heapq.heappush(pq, (dist[nn], nn))

    return -1

d = dij(seen[S], seen[T], g)
print(d)