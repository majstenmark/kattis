import math

def topf(n, k):
    v = 1
    for nn in range(n, n - k, -1):
        v *= nn
    return v

def fac(k):
    return math.factorial(k)

N, P  = map(int, raw_input().split())

bestprob = 0.0
rest = topf(N, P-1)/fac(P-1)

pfac = fac(P)
f = topf(N, P)* 1.0/pfac
T_old = N
for m in range(1, 4 * N):
    T_new = T_old + 1
    f = f/(T_old - P + 1) * T_new
    prob = m * rest * 1.0/f
    if prob < bestprob:
        break
    bestprob = max(bestprob, prob)
    T_old = T_new
print bestprob
