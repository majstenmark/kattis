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

def solve(k):
    f0, f1 = 1, 1
    S = {}
    for i in range(2, k+10):
        f0, f1 = f1, f0 + f1
        if f1%k in S:
            return S[f1%k]
        S[f1%k] = i
Q = ni()
for _ in range(Q):
    k = ni()
    print(solve(k))


