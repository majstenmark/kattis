from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s): sys.stderr.write('{}\n'.format(s))
def ni(): return int(inp())
def nl(): return [int(_) for _ in inp().split()]

N = ni()
K = nl()
MIN = min(K)*4
MAX = max(K)*4
avg = sum(K)*4.0/N

import cmath


# A has to be of length a power of 2.
def FFT2(a, inv=False):
    N = len(a)
    j = 0
    for i in range(1, N):
        bit = N>>1
        while j&bit:
            j ^= bit
            bit >>= 1
        j^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    L = 2
    MUL = -1 if inv else 1
    while L <= N:
        ang = 2j*cmath.pi/L * MUL
        wlen = cmath.exp(ang)
        for i in range(0, N, L):
            w = 1
            for j in range(L//2):
                u = a[i+j]
                v = a[i+j+L//2] * w
                a[i+j] = u + v
                a[i+j+L//2] = u - v
                w *= wlen
        L *= 2
    if inv:
        for i in range(N):
            a[i] /= N
    return a

sz = 2**18

def pow4(K1):
    f1 = FFT2(K1)
    v = [(a*a) for a in f1]
    K2 = [round(x.real) > 0 for x in FFT2(v, True)]
    f2 = FFT2(K2)
    v = [(a*a) for a in f2]
    return [round(x.real) > 0 for x in FFT2(v, True)]
    

K1 = [0]*sz
for k in K:
    K1[k] = 1

K4 = pow4(K1)
S = [i for i, v in enumerate(K4) if v]
print(' '.join(map(str, [MAX, MIN, len(S), avg])))


