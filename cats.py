import sys
from heapq import heappop as pop, heappush as push, heapify

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())
T = ni()
for _ in range(T):
    M, C = nl()
    L = C*(C-1)//2
    confl = [nl() for _ in range(L)]
    edges = [[] for _ in range(C)]
    for i, j, D in confl:
        edges[i].append((D, j))
        edges[j].append((D, i))
    tree = set([0])
    ne = edges[0]
    heapify(ne)
    dist = 0
    while len(tree) < C:
        d, alt = pop(ne)
        while alt in tree:
            d, alt = pop(ne)
        dist += d
        tree.add(alt)
        for di, i in edges[alt]:
            push(ne, (di, i))
    #print(dist)
    if dist + C <= M:
        print('yes')
    else:
        print('no')


        
