from collections import *
try: inp = raw_input
except: inp = input
def ni(): return int(inp())
def nl(): return [int(x) for x in inp().split()]

N = ni()

lo = 1.0
hi = 30.0

for _ in range(100):
    mid = (lo + hi)/2
    if mid**mid < N:
        lo = mid
    else:
        hi = mid
print(lo)