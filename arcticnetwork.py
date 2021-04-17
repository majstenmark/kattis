import sys
from heapq import heappush as push, heappop as pop, heapify as heapify

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def dist2(p1, p2):
    return (p1[0] - p2[0]) **2 + (p1[1] - p2[1])**2

T = ni()
for _ in range(T):
    S, N = nl()
    coord = [nl() for _ in range(N)]
    g = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            p1 = coord[i]
            p2 = coord[j]
            d = dist2(p1, p2)
            g[i].append((d, j))
            g[j].append((d, i))

    used = set([0])
    edges = g[0]
    heapify(edges)
    usededges = []
    while len(used) < N:
        d, i = pop(edges)
        if i not in used:
            used.add(i)
            usededges.append(d)
            for d2, e2 in g[i]:
                push(edges, (d2, e2))
    usededges.sort()
    mx = usededges[-S]
    ans = mx**0.5
    print('{:.2f}'.format(ans))
   
