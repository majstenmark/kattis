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

S = inp()

X = list(S)
X.sort()
if X[0] == X[-1]:
    print(-1)
    exit()
C = Counter()
for ch in S:
    C[ch] += 1
X.sort(key=lambda x: (-C[x], x))
N = len(S)//2
X[N], X[-1] = X[-1], X[N]
print(''.join(X))
