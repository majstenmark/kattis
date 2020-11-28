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

def sc(c):
    if c == 'T': return 10
    if c == 'J': return 11
    if c == 'Q': return 12
    if c == 'K': return 13
    if c == 'A': return 14
    return int(c)

def score(X, Y, offset):
    pts = 0
    N = len(X)
    for i in range(len(X)):
        x = X[i]
        y = Y[(i+offset)%N]
        if x == y: pts += 1
        if x < y: pts += 2
    return pts

def solve():
    X = [sc(c) for c in inp()]
    Y = [sc(c) for c in inp()]
    X.sort()
    Y.sort()
    MAX = 0
    for i in range(len(X)):
        MAX = max(MAX, score(X, Y, i))
    print(MAX)
N = ni()
for _ in range(N):
    solve()
