import math

tol = 10 **-7

D, S = map(int, raw_input().split())
aMax = max(10**20, D*10)
a = aMax
b = D*1.0/(2.0 *a)
val = 10**3
aMin = 0.0
count = 0
while abs(val) > tol:
    a = (aMax + aMin)/2.0
    count += 1
    b = D*1.0/(2.0 *a)
    val = a * math.cosh(b) - a - S
    if val > 0:
        aMin = a
    else:
        aMax = a

length = 2*a *math.sinh(D/(2.0*a))
print(length)
