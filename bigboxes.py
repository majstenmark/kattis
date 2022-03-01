import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N, K = nl()
W = nl()

def test(mx):
    box = 0
    bw = 0
    for w in W:
        if w > mx: return False
        if bw + w <= mx:
            bw += w
        else:
            box += 1
            bw = w
    return box < K

lo = 0
hi = N * max(W) +1
while lo < hi:
    mid = (lo + hi)//2
    if test(mid):
        hi = mid
    else:
        lo = mid+1
print(lo)
