

import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)

def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

from decimal import Decimal

def solve(k, n, e):
    N = pow(2,n)
    deg = [0] * N
    g = [[] for _ in range(N)]
    for _ in range(e):
        v1, v2 = nl()
        g[v1].append(v2)
        g[v2].append(v1)
        deg[v1] += 1
        deg[v2] += 1

    s = 1.0/N
    probs = [s for _ in range(N)]
    nextprobs = [0.0] * N

    for step in range(1,k):
        for node in range(N):
            p = probs[node]
            for ne in g[node]:
                transprob = p/deg[node]
                nextprobs[ne] += transprob
        bits = [0] * n
        for i in range(N):
            for b in range(n):
                if 2 ** b & i:
                    bits[b] += nextprobs[i]
        for b in bits:
            
            if not (1 < 4*b < 3):
                return 'No'
        probs = nextprobs
        nextprobs = [0.0] * N

    return 'Yes'

k, n, e = nl()
while k != 0:
    s = solve(k, n,e)
    print(s)
    
    k, n, e = nl()
