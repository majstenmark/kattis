import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
A = [ni() for _ in range(N)]
#choose k
prod = 0
su = sum(A)
best = 0
for a in A:
    prod += a**2
    su -= a
    alt = prod * su
    best = max(best, alt)
print(best)
