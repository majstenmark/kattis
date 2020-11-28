from math import sin, pi
H, V = [int(v) for v in raw_input().split()]
if V <= 180:
    print('safe')
else:
    alpha = (V -180)/180.0 * pi
    D = H / sin(alpha)
    s=int(D)
    print(s)