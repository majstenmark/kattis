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

def offsets(A, B):
    N = len(A)
    offs = []
    for i in range(N):
        ok = True
        for j in range(N):
            if A[j] == B[(i+j)%N]:
                ok = False
                break
        if ok: offs.append(i)
    return offs

A, B, C = [inp() for _ in range(3)]
AB = offsets(A, B)
BC = set(offsets(B, C))
AC = offsets(A, C)
N = len(A)
INF = 10**10
BEST = INF
for dab in AB:
    for dac in AC:
        dbc = (dac - dab + N)%N
        if dbc in BC:
            x, y, z = min(dab, N - dab), min(dac, N - dac), min(dbc, N - dbc)
            BEST = min(BEST, x + y)
            BEST = min(BEST, x + z)
            BEST = min(BEST, z + y)
if BEST == INF: BEST = -1
print(BEST)

