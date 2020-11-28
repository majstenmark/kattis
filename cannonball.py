import math
g = 9.81

N = int(raw_input())
for n in range(N):
    v0, theta, x1, h1, h2 = [float(v) for v in raw_input().split()]
    thetaRad = theta * math.pi/180
    t = x1 / (v0 * math.cos(thetaRad))
    y = v0 * t* math.sin(thetaRad) - 0.5 * g * t **2
    if h1 + 1 <= y <= h2 -1:
        print('Safe')
    else:
        print('Not Safe')  