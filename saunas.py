import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def f(a, b, c, x):
    return a * x**2 + b * x + c

def getmx(lo, hi, A, B, C):
    alt1 = 0
    if A != 0:
        x = - B/(2 * A)
        if lo <= x <= hi:
            alt1 = f(A, B, C, x)
    alt2 = f(A, B, C, lo)
    alt3 = f(A, B, C, hi)
    return max(alt1, alt2, alt3)
    


N = ni()
finns = [nl() for _ in range(N)]
toughest = [(t, a, b, c) for a, b, c, t in finns]
toughest.sort(reverse = True)
A, B, C = 0, 0, 0
best = 0.0
if N == 1:
    t, a, b, c = toughest[0]
    best = getmx(0, t, a, b, c)
    print(best)
else:
    for i in range(N):
        t, a, b, c = toughest[i]
        A += a
        B += b
        C += c

        alt = getmx(0, t, A, B, C)
        best = max(best, alt)
    print(best)
