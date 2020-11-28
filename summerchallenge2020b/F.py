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

def red(n):
    p = 1
    for i in map(int, n):
        if i != 0: p*=i
    if p < 10: return p
    return red(str(p))

def prods(k, i):
    if i == 0: return k
    return k*i

def solve(L):
    if L == 0:
        return {}
    prMAX = {1:1}
    prOther = {}
    for d in map(int, str(L)):
        prMAX2 = Counter()
        prOTHER2 = Counter()
        for k, v in prMAX.items():
            for i in range(d):
                prOTHER2[prods(k, i)] += v
            prMAX2[prods(k, d)] += v
        for k, v in prOther.items():
            for i in range(10):
                prOTHER2[prods(k, i)] += v
        prMAX = prMAX2
        prOther = prOTHER2
    for k, v in prMAX.items():
        prOther[k] += v
    prOther[1] -= 1
    out = Counter()
    for k, v in prOther.items():
        out[red(str(k))] += v

    return out


L, R = nl()

sl = solve(L-1)
sr = solve(R)
for k, v in sl.items():
    sr[k] -= v
print(' '.join(str(sr[i]) for i in range(1, 10)))
