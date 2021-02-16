import sys
from math import sin, cos

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def price(k):
    return p * (sin(a * k + b) + cos(c * k + d) + 2)

p, a, b, c, d, n = nl()
mx = 0
top = 0
curr = 0
for k in range(1, 1 + n):
    pr = price(k)
    top = max(top, pr)
    mx = max(mx, top - pr)
    curr = pr
print(mx)
