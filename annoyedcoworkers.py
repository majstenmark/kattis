import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

H, C = nl()
cow = [nl() for _ in range(C)]

def test(mx):
    cnt = 0
    for a, d in cow:
        k = (mx - a)//d
        cnt += k
    return cnt >= H

mn = 0
for a, _ in cow:
    mn = max(mn, a)
lo = mn

hi = 10**14 + 10**9
while lo < hi:
    mid = (lo + hi)//2
    if test(mid):
        hi = mid
    else:
        lo = mid+1
    
print(hi)
