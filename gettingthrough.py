import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())


T = ni()

for _ in range(T):
    W = ni()
    N = ni()
    sensors = [nl() for _ in range(N)]
    size = [1] * (N + 2)
    components = [i for i in range(N+2)]
   
    def find(x):
        if components[x] != x:
            components[x] = find(components[x])
        return components[x]

    def union(a_comp,b_comp):       
        if size[a_comp] < size[b_comp]:
            small, large = a_comp, b_comp
        else:
            small, large = b_comp, a_comp
        
        size[large] += size[small]
        components[small] = large
        
        
    def toside(n, X):
        x, y, r = sensors[n]
        return max(0, abs(X - x) - r)

    def dist(i, j):
        x, y, r = sensors[i]
        x2, y2, r2 = sensors[j]
        dx = abs(x - x2)
        dy = abs(y - y2)
        d = (dx**2 + dy **2) **0.5
        sep = max(0, d - r - r2)
        return sep

    
    edges = []
    S1 = N
    S2 = N+1
    sm = W
    for i in range(N):
        s1 = toside(i, 0)
        if s1 == 0:
            components[i] = S1
        else:
            edges.append((i, S1, s1))
        s2 = toside(i,W)
        if s2 == 0:
            components[i] = S2
        else:
            edges.append((i, S2, s2))
        sm = min(sm, max(s1, s2))

    for i in range(N):
        for j in range(i + 1, N):
            ri = find(i)
            rj = find(j)
            if ri == rj: continue
            s3 = dist(i, j)
            if s3 == 0:
                union(ri, rj)
            elif s3 < sm:

                edges.append((i, j, s3))
                
    edges.sort(key = lambda x: x[2]) #sort by weight!
        
    w = sm
    if find(N) != find(N+1):
        for u, v, w in edges:
            u_comp = find(u)
            v_comp = find(v)
            if u_comp != v_comp:
                union(u_comp, v_comp)
                if find(N) == find(N+1):
                    break

        print(w/2)
    else:
        print(0)


