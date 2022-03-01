import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

R, C = nl()
rows = nl()
cols = nl()
if max(rows) == max(cols):
    print('possible')
else:
    print('impossible')