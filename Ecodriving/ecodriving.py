import heapq
import math
# Dijkstra from S to T
INF = 10**12
ang = {}
def angle(j1,j2,j3):
    #if (j1,j2,j3) in ang: return ang[j1,j2,j3]
    p1 = junct[j1]
    p2 = junct[j2]
    p3 = junct[j3]
    v1 = p2[0] - p1[0], p2[1] - p1[1]
    v2 = p3[0] - p2[0], p3[1] - p2[1]
    absv1 = math.sqrt(v1[0] ** 2+ v1[1] **2)
    absv2 = math.sqrt(v2[0] ** 2+ v2[1] **2)
    scalar = v1[0] * v2[0] +v1[1] * v2[1]
    q = scalar/absv1/absv2

    try:
        ret = math.acos(q)
    except:
        ret = math.pi/2
    #ang[j1,j2,j3] = ret
    return ret

def distance(j1,j2):
    deltaX = junct[j1][0] - junct[j2][0]
    deltaY = junct[j1][1] - junct[j2][1]
    return math.sqrt(deltaX **2 +deltaY ** 2)

from collections import defaultdict
def dij(maxAngle):
    dist = defaultdict(lambda:INF)

    pq = []
    for de, ne in g[0]:
        pq.append((de, ne, 0))
        dist[0,ne] = de
    heapq.heapify(pq)
    while pq:
        (nd, node, prev) = heapq.heappop(pq)
        for (dd, nn) in g[node]:
            if(angle(prev,node, nn) <= maxAngle):
        #        print 'ok'
                alt = dist[prev,node] + dd
                if dist[node,nn] > alt:
                    dist[node,nn] = alt
                    heapq.heappush(pq, (dist[node,nn], nn,node))
    #print 'dist ', dist
    return min(dist[i, J-1] for i in range(J)) <= D

J, R, D = map(int, raw_input().split())
junct = []

for j in range(J):
    x, y = map(int, raw_input().split())
    junct.append((x,y))

g = [[] for _ in range(J)]
for r in range(R):
    a,b = map(int, raw_input().split())
    g[a-1].append((distance(a-1,b-1),b-1))

minA = 0.0
maxA = math.pi
solvable = dij(maxA)
minSolv = dij(minA)
if not solvable:
    print 'Impossible'
    exit()
if minSolv:
    print 0.0
else:
    mid = (maxA + minA)/2
    #print 'binary searching ...', mid, maxA
    #while abs(mid - maxA) > 10 ** -6:
    for i in range(50):
        mid = (minA +maxA)/2
    #    print 'mid', mid
        so = dij(mid)
        if so:
    #        print 'udated maxA', mid
            maxA = mid
        else:
            minA = mid



    s = '{}'.format(maxA/math.pi * 180)
    print(s)
