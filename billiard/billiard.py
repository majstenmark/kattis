import math

a, b, s, m, n = map(int, raw_input().split())
while s != 0:
    vv =n*b*1.0/s
    vh = m*a*1.0/s
    v = math.sqrt(vv**2 + vh**2)
    angle = math.asin(vv*1.0/v) * 180.0 / math.pi
    
    s = '{:.2f} {:.2f}'.format(angle, v)
    print(s)
    a, b, s, m, n = map(int, raw_input().split())
