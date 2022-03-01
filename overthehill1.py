import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
mat = [nl() for _ in range(N)]
plaintext = inp()
txt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
MAP1 = {}
MAP2 = {}
for i, lt in enumerate(txt):
    MAP1[lt] = i
    MAP2[i] = lt

digits = []
for lt in plaintext:
    digits.append(MAP1[lt])

vectors = [[]]
for d in digits:
    if len(vectors[-1]) == N:
        vectors.append([])
    if len(vectors[-1]) < N:
        vectors[-1].append(d)
    

while len(vectors[-1]) < N:
    vectors[-1].append(36)
    

def apply(v, mat):
    res = []
    for row in mat:
        su = 0
        for i in range(len(v)):
            su += row[i] * v[i]
            su %= 37
        res.append(su)
    return res


out = []
for v in vectors:

    trans = apply(v, mat)
    for t in trans:
        out.append(MAP2[t])

print(''.join(out))