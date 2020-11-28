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

N = ni()
a = []
b = []
for _ in range(N):
    aa, bb = nl()
    a.append(aa)
    b.append(bb)
SA = sum(a)
SB = sum(b)
A = [SA]*N
B = [SB]*N
for i in range(N):
    A[i] -= a[i]
    B[i] -= b[i]


rm1 = sum(aa*(aa-1)//2*bb for aa,bb in zip(a, b))
rm2 = sum(ai*(ai-1)//2*Bi for ai, Bi in zip(a, B) )
rm3 = sum(ai*Ai*bi for ai, Ai, bi in zip(a, A, b) )
SUM = SB*SA*(SA-1)//2
print(SUM - rm1 - rm2 - rm3)
