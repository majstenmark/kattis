from math import sin, cos, pi
N = int(raw_input())
for n in range(N):
    M = int(raw_input())
    currang = 90
    x, y = 0.0, 0.0
    for m in range(M):
        ang, dist = [float(v) for v in raw_input().split()]
        currang += ang
        currang %= 360.0
        rad = currang *pi / 180
        deltay = dist * sin(rad)
        deltax = dist * cos(rad)
        x += deltax
        y += deltay
    print('{} {}'.format(x, y))
        
