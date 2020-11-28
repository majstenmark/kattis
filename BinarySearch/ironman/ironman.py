import math

xs, ys,xf,yf = map(float, raw_input().split())
n = int(raw_input())
layers = [ys] + [float(v) for v in raw_input().split()] + [yf]
speeds = [float(v) for v in raw_input().split()] + [1.0]
D = abs(xf - xs)

def run(alpha1):
    time = 0.0
    dist = 0.0
    for k in range(n):
        hk = layers[k+1] - layers[k]
        s1 = speeds[k]
        s2 = speeds[k+1]
        res = s2* math.sin(alpha1)/s1
        if abs(res) > 1:
            return 10**12, 10**12
        alpha2 = math.asin(res)
        hyp = hk/ math.cos(alpha1)
        dist += math.tan(alpha1)* hk
        time += hyp/s1
        alpha1 = alpha2
    return time, dist

maxAngle = math.pi/2
minAngle = 0.0

calcDist = 10** 20
for i in range(50):
    mid = (maxAngle + minAngle)/2
    calcTime, calcDist = run(mid)
    if calcDist > D:
        maxAngle = mid
    else:
        minAngle = mid

print(calcTime)
