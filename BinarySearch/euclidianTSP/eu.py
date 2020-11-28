import math

i = raw_input().split()
N = int(i[0])
P = float(i[1])
S = float(i[2])
V = float(i[3])
k1 = N * 1.0/(P * 10**9)
sq2 = math.sqrt(2)
logn = math.log(N, 2)
sp1 = S/V
cHigh = 100
cLow = 0
tol = 10**-8

def ev(c):

    return k1*(logn ** (c*sq2)) + keys(c)

def keys(c):
    return S *1.0/V*(1.0 + 1.0/c)

while abs(cHigh - cLow) > tol:
    third = (cHigh - cLow)*1.0/3
    cut1 = cLow + third
    cut2 = cLow + 2* third
    f1 = ev(cut1)
    f2 = ev(cut2)
    if f2 > f1:
        cHigh = cut2
    else:
        cLow = cut1

print('{} {}'.format(f1, cLow))
