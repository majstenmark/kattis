from collections import *
import sys
sys.setrecursionlimit(10000)
inp = input
def ni(): return int(inp())
def nl(): return [int(v) for v in inp().split()]

ONE = 'BFPV'
TWO = 'CGJKQSXZ'
D = {'D' : 3, 'T': 3,
'L' : 4,
'M' : 5, 'N': 5,
'R' : 6}
for o in ONE: D[o] = 1
for t in TWO: D[t] = 2

last = None
for line in sys.stdin:
    s = ''
    for ch in line:
        if ch in D:
            d = D[ch]
            if d != last:
                s += str(d)
            last = d
        else:
            last = None
    print(s)
