import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
keywords = set()
for _ in range(N):
    w = inp()
    w = w.replace('-', ' ').lower()
    keywords.add(w)
print(len(keywords))