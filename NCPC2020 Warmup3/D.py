from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s):
    sys.stderr.write('{}\n'.format(s))

def ni():
    return int(inp())

def nl():
    return [int(_) for _ in inp().split()]


def solve(i, lo, hi):
    if lo == hi:
        if lo in R: return
        sols.append(i)
        return
    fail = False
    for r in R:
        if lo <= r <= hi:
            fail = True
            break
    if not fail:
        sols.append(i)
    else:
        mid = (lo + hi)//2
        solve(i*2, lo,mid)
        solve(i*2 + 1, mid + 1, hi)
sols = []

n, _ = nl()
R = nl()

solve(1, 2**n, 2**(n+1) - 1)
sols.sort()
print(' '.join(map(str, sols)))


