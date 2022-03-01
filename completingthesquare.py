import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

corners = [nl() for _ in range(3)]

def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def tip(c, others):
    p0 = corners[c]
    p1 = corners[others[0]]
    p2 = corners[others[1]]
    
    d1 = dist(p0, p1)
    d2 = dist(p0, p2)
    return d1 == d2

def vec(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]

for c in range(3):
    others = [i for i in range(3) if i != c]
    
    if tip(c, others):
        p0 = corners[c]
        p1 = corners[others[0]]
        p2 = corners[others[1]]
        v1 = vec(p0, p1)
        v2 = vec(p0, p2)
        x = p0[0] + v1[0] + v2[0]
        y = p0[1]+ v1[1] + v2[1]
        print(x, y)
        