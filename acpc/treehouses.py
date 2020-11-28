import math
from heapq import heappush, heappop
# get all connected components
# union find

def dist2(p1, p2):
    return (p2[0]- p1[0]) ** 2 + (p2[1]- p1[1]) ** 2

def addall(q, n, found):
    for w in wires[n]:
    #    print 'from wires', 0, n, w
        heappush(q,(0, n, w))
    if n > 0:
        for p in range(1, N+1):
            if p != n and p not in found:
                d2 = dist2(houses[n-1], houses[p-1])
            #    print 'fdfd', d2, n-1, p-1
                heappush(q,(d2, n, p))


N, E, P = map(int, raw_input().split())
houses = []
g = [[] for _ in range(N+1)]
q = [(0, 0, e) for e in range(1, E+1)]
wires = [[] for _ in range(N+1)]

found = set([0])


for n in range(N):
    x, y = map(float, raw_input().split())
    houses.append((x, y))

for p in range(P):
    a, b = map(int, raw_input().split())
    wires[a].append(b)
    wires[b].append(a)

tot = 0.0
cnt = 1
#print wires
while q and len(found) <= N:
    d, u, v = heappop(q)
#    print d, u, v
    if u not in found:
        found.add(u)
        addall(q, u, found)
        tot += math.sqrt(d)

    if v not in found:
        found.add(v)

        addall(q, v, found)
        tot += math.sqrt(d)

print tot
