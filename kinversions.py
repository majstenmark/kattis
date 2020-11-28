# DID NOT PASS< TLE

import cmath
# A has to be of length a power of 2.
def FFT(A, inverse=False):
    N = len(A)
    if N <= 1: 
        return A
    if inverse:
        D = FFT(A) # d_0/N, d_{N-1}/N, d_{N-2}/N, ...
        return map(lambda x: x/N, [D[0]] + D[:0:-1])
    evn = FFT(A[0::2])
    odd = FFT(A[1::2])
    Nh = N//2
    return [evn[k%Nh]+cmath.exp(2j*cmath.pi*k/N)*odd[k%Nh]
            for k in range(N)]

def round_up(n):
    while n&(-n) != n:
        n += n&(-n)
    return n

def pad(P):
    sz_P = round_up(len(P))
    P.extend([0]*(sz_P*2 - len(P)))
    return P


def poly_mul(P, Q):
    P = pad(P)
    Q = pad(Q)
    P_f = FFT(P)
    Q_f = FFT(Q)
    Z = [p*q for p, q in zip(P_f, Q_f)]
    return [int(round(r.real)) for r in FFT(Z, True)]

S = input()
N = len(S)
b_pol = [1 if S[i]== 'B' else 0 for i in range(N)]

a_pol = [1 if S[N - i -1]== 'A' else 0 for i in range(N)]

c_pol = poly_mul(a_pol, b_pol)
for i in range(1, N):
    print('{:.0f}'.format(c_pol[N-i-1]))