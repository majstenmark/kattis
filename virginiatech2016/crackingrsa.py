from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s): sys.stderr.write('{}\n'.format(s))
def ni(): return int(inp())
def nl(): return [int(_) for _ in inp().split()]

def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = (a // b, b, a % b)
        x0, x1 = (x1, x0 - q * x1)
        y0, y1 = (y1, y0 - q * y1)
    return (a, x0, y0)
def inv(a, M):
    return xgcd(a, M)[1]%M

T = ni()
for _ in range(T):
    n, e = nl()
    for i in range(2, n):
        if n%i == 0: break
    p, q = i, n//i
    phi = (p-1)*(q-1)
    d = inv(e, phi)
    print(d)

