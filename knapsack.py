import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    path = [[(0, 0) for x in range(W + 1)] for x in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                alt1 = val[i-1] + K[i-1][w-wt[i-1]]
                alt2 = K[i-1][w]
                if alt1 > alt2:
                    K[i][w] = alt1
                    path[i][w] = (i-1, w-wt[i-1])
                else:
                    K[i][w] = alt2

                    path[i][w] = (i-1, w)
            else:
                K[i][w] = K[i-1][w]
                path[i][w] = (i-1, w)
    indeces = []
    pi, pw = n, W
    ni, nw = path[n][W]
    while pw > 0:
        if pw > nw:
            indeces.append(ni)
        pi, pw = ni, nw
        ni, nw = path[ni][nw]
        

    return indeces[::-1]

out = []
while True:
    try:    
        C, N = nl()
        val = [0] * N
        ws = [0] * N
        for i in range(N):
            v, w = nl()
            val[i] = v
            ws[i] = w
        r = knapSack(C, ws, val, N)
        out.append(str(len(r)))
        s = ' '.join(map(str, r))
        out.append(s)
    except:
        break
print('\n'.join(out))
