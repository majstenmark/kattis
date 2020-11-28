from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s): sys.stderr.write('{}\n'.format(s))
def ni(): return int(inp())
def nl(): return [int(_) for _ in inp().split()]


def picks(left, last):
    if len(left) == 0: return [[]]
    orders = []
    for n in range(N):
        if n in left and last not in G[n]:
            left.remove(n)
            L = picks(left, n)
            left.add(n)
            for l in L:
                l.append(n)
                orders.append(l)
    return orders

T = ni()
for _ in range(T):
    N = ni()
    V = inp().split()
    ID = {k: i for i, k in enumerate(V)}
    G = [set() for _ in range(N)]
    M = ni()
    for _ in range(M):
        a, b = inp().split()
        a_i = ID[a]
        b_i = ID[b]
        G[a_i].add(b_i)
        G[b_i].add(a_i)
    S = set(range(N))
    fst = None
    L = picks(S, None)
    no = len(L)
    o = L[0]
    print(no)
    print(' '.join(V[k] for k in o[::-1]))
    


    
