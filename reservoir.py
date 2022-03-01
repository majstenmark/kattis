import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop
import bisect

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def solve(N, L, H, queries):
    #print here
    dw = L[0]
    precomp = [dw * H[0]]
    water = precomp[0]
    stack = [0]

    for i in range(1, N):
        #if higher than prev
        if H[i] > H[i-1]:
            dw = L[i] - L[i-1] - 1
            water += dw * H[i - 1]
            prevh = H[i - 1]
            #print('tmp', dw, H[i - 1], water)
            #print('stack', stack)
            while len(stack) > 0 and H[stack[-1]] <= H[i]:
                dh = H[stack[-1]] - prevh
                dw = L[i] - L[stack[-1]] - 1
                prevh = H[stack[-1]]
                #print('dw, dh', dw, dh)
                water += dh * dw
                stack.pop()
            dh = H[i] - prevh
            dw = L[i]
            if len(stack) > 0:
                dw = L[i] - L[stack[-1]] - 1
            #print('last ', dh, dw, prevh)
            water += dh * dw    
            precomp.append(water)
            stack.append(i) 
        else:
            #same or lower
            dw = L[i] - L[i-1] - 1
            water += dw * H[i]
            #print('lower ', dw, H[i])
            precomp.append(water)
            stack.append(i)
    out = []
    print(precomp)
    for q in queries:
        index = bisect.bisect_left(precomp, q)
        out.append(str(index))
    print('\n'.join(out))
    




T = ni()
for _ in range(T):
    N = ni()
    L = nl()
    H = nl()
    Q = ni()
    queries = [ni() for _ in range(Q)]
    solve(N, L, H, queries)
