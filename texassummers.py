import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())


import heapq

def genpath(parents, S, T):
    path = []
    p = parents[T]
    while p != S:
        path.append(p)
        p = parents[p]
    return path[::-1] if len(path) > 0 else ['-']

def gen(node, MAX):
    ne = []
    for i in range(len(nodes)):
        d = d2(nodes[node], nodes[i])

        if d < MAX and node != i:
            ne.append((d, i))
    return ne

def dij(S, T,MAX):
    #g list with lists with tuples distance, other node
    # Dijkstra from S. Check t optionally
    INF = 10**12
    dist = [INF for _ in range(N+2)]
    parents = [0]  * (N+ 2)
    pq = []
    dist[S] = 0
    pq.append((0, S))
    heapq.heapify(pq)
    while pq:
        (nd, node) = heapq.heappop(pq)
        if nd != dist[node]: continue
        #if node == T: return dist[T]
        if node == T: return genpath(parents, S, T)
        for (dd, nn) in gen(node, MAX - dist[node]):
            alt = dist[node] + dd
            if dist[nn] > alt and alt < MAX:
                dist[nn] = alt
                parents[nn] = node
                heapq.heappush(pq, (dist[nn], nn))

    return ['-']

def d2(p, q):
    return pow(p[0] - q[0], 2) + pow(p[1] - q[1], 2)

N = ni()
shade = [nl() for _ in range(N)]
start= nl()
cl = nl()
nodes = shade + [start]+ [cl]
MAX = d2(start, cl)

path = dij(N, N+1, MAX)
print('\n'.join(map(str, path)))
        