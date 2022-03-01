import sys
from collections import defaultdict as dd, Counter
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

T = ni()
out = []
for _ in range(T):
    N = ni()
    cnt = Counter()
    for _ in range(N):
        name, cat = inp().split()
        cnt[cat] += 1
    p = 1
    for cat, c in cnt.items():
        p *= (c + 1)
    out.append(str(p -1))
    
print('\n'.join(out))

