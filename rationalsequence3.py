import sys
import math
itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def left(p, q):
    return p, p+q

def right(p, q):
    return p+q, q


def solve(n):
    h = int(math.log(n, 2))
    inlayer = 2 ** h
    below = inlayer -1
    no_in_layer = n - below
    lo = 1
    hi = inlayer
    p = q = 1
    while lo < hi:
        mid = (lo + hi)//2
        if no_in_layer <= mid:
            p, q = left(p, q)
            hi = mid
        else:
            p, q = right(p, q)
            lo = mid + 1
    return p, q


P = ni()
for p in range(P):
    k, n = nl()
    p, q = solve(n)
    print(f'{k} {p}/{q}')