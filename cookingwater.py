import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
intervals = [nl() for _ in range(N)]
times = [0] * 1001
for a, b in intervals:
    for t in range(a, b+1):
        times[t] += 1
for v in times:
    if v == N:
        print('gunilla has a point')
        exit()
print('edward is right')