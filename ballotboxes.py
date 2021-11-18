import sys
from heapq import heappush as push, heappop as hpop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def test(no, pop, allowed):
    needed = 0
    for p in pop:
        used = (p+ no -1)//no
        needed += used
    return needed <= allowed

def solve(N, B, pop):
    hi = sum(pop) #working
    lo = 0 #not allowed
    while lo < hi:
        mid = (lo + hi)//2
        if test(mid, pop, B):
            hi = mid
        else:
            lo = mid +1
    return hi

while True:

    N, B = nl()
    if N == -1: break
    
    pop = [ni() for _ in range(N)]
    inp()
    r = solve(N, B, pop)
    print(r)

    