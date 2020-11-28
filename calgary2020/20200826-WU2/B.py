from collections import *
import sys, cmath
try: inp = raw_input
except: inp = input
def err(s): sys.stderr.write('{}\n'.format(s))

def ni(): return int(inp())

def nl(): return [int(_) for _ in inp().split()]

def parse():
    x, no = inp().split()
    return float(x), int(no)

def cnt(n):
    return bin(n).count('1')

# A has to be of length a power of 2.
def FFT(A, inverse=False):
    N = len(A)
    if N <= 1: 
        return A
    if inverse:
        D = FFT(A) # d_0/N, d_{N-1}/N, d_{N-2}/N, ...
        return [x/N for x in ([D[0]] + D[:0:-1])]
    evn = FFT(A[0::2])
    odd = FFT(A[1::2])
    Nh = N//2
    return [evn[k%Nh]+cmath.exp(2j*cmath.pi*k/N)*odd[k%Nh]
            for k in range(N)]

def polymul(A, B):
    F1 = FFT(A)
    F2 = FFT(B)
    FM = [x*y for x, y in zip(F1, F2)]
    return [ci.real for ci in FFT(FM, inverse=True)]


k, v = nl()

TEST = False

MOD = 1<<k
B = [cnt(i) for i in range(MOD)]

DP = [0.0]*MOD
DP[0] = 1.0
for _ in range(v-1):
    p0, no = parse()
    DP2 = [0.0]*MOD
    for c, p in enumerate(DP):
        DP2[c] += p*(1-p0)
        DP2[(c+no)%MOD] += p*p0
    DP = DP2
P = DP

def get_ans():
    ans = [0]*MOD
    for j in range(MOD):
        for i in range(MOD):
            ans[j] += P[i]*B[(i+j)%MOD]
        print(j, ans[j])
    return ans
if TEST:
    ans = get_ans()

P = P[::-1]
V = polymul(P, B)
V = [V[-1]] + V[:-1]
M = -1, -1
for i, x in enumerate(V):
    if TEST:
        assert abs(x - ans[i]) < 0.0001, '{} {} {}'.format(i, x, ans[i])
    M = max(M, (x, i))

print(M[1])

