import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def nll(): return [int(v)-1 for v in inp().split()]
def ni(): return int(inp())
INF = 10**60

import heapq

def dij(S, G):
    
    N = len(G)
    dist = [INF for _ in range(N)]

    pq = []
    dist[S] = 0
    #onpath = [False] * N
    pq.append((0, S))
    heapq.heapify(pq)
    
    while pq:
        (nd, node) = heapq.heappop(pq)
        #if node == h or node == g:
        #    onpath[node] = True
        if nd > dist[node]: continue
        #if node == T: return dist[T]
        for (dd, nn) in G[node]:
            alt = dist[node] + dd
            if dist[nn] > alt:
                dist[nn] = alt
                #onpath[nn] = onpath[nn] or onpath[node]
                heapq.heappush(pq, (dist[nn], nn))
            
    return dist


T = ni()
for _ in range(T):
    N, m, t = nl()
    s, g, h = nll()
    G = [[] for _ in range(2*N)]
    for _ in range(m):
        a, b, d = nl()
        a, b = a-1, b-1
        if (a == g and b == h) or (a == h and b == g):
            G[a].append((d, b+N))
            G[b].append((d, a+N))
        else:
            G[a].append((d, b))
            G[b].append((d, a))
            G[a+N].append((d, b+N))
            G[b+N].append((d, a+N))
            
        
        
    
    targets = set([(ni()-1) for _ in range(t)])
    dists = dij(s, G)
    ok = []
    print(dists)
    for t in targets:
        if dists[t+N] < INF:
            ok.append(t+1)
    ok.sort()
    print(' '.join(map(str, ok)))

