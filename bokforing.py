from collections import defaultdict as dd
import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

X = 0
def default(): return X
N, Q = nl()
ppl = dd(default)
out = []
for _ in range(Q):
    op = inp().split()
    if op[0] == 'SET':
        i, x = map(int, op[1:])
        ppl[i] = x
    if op[0] == 'PRINT':
        i = int(op[1])
        out.append(str(ppl[i]))
    if op[0] == 'RESTART':
        X = int(op[1])
        ppl = dd(default)
print('\n'.join(out))
