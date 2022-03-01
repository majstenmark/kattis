import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

T = ni()
out = []
for _ in range(T):
    N, M = nl()
    for _ in range(M):
        nl()
    out.append(str(N-1))
print('\n'.join(out))

