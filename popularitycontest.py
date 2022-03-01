import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def nl1(): return [int(v)-1 for v in inp().split()]
def ni(): return int(inp())

N, M = nl()
edges = [nl1() for _ in range(M)]

friends = [0] * N
for a, b in edges:
    friends[a] += 1
    friends[b] += 1

coeff = ['0'] * N
for i in range(1, N+1):
    no_friends = friends[i-1]
    coeff[i-1] = str(no_friends - i)
print(' '.join(coeff))
