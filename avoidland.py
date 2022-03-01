import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def align(pos):
    pos.sort()
    diff = 0
    for i, p in enumerate(pos):
        diff += abs(i+1 - p)
    return diff
        



N = ni()
pos = [nl() for _ in range(N)]
rows = []
cols = []
for r, c in pos:
    rows.append(r)
    cols.append(c)
moves = align(rows)
moves += align(cols)
print(moves)