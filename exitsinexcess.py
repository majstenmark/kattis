import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N, M = nl()
edges = [nl() for _ in range(M)]
inc = set()
dec = set()
for i, (u, v) in enumerate(edges):
    if u < v:
        inc.add(i)
    else:
        dec.add(i)
out = []
if len(inc) < len(dec):
    for i in inc:
        out.append(str(i+1))
else:
    for i in dec:
        out.append(str(i+1))
print(len(out))
if len(out) > 0: print('\n'.join(out))