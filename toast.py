import math
N, D, T = [int(v) for v in input().split()]
D2 = 2 * D

def mx():
    cnt = 0
    no = 2 * T//N
    per_side = (no+1)//2
    alpha = 2 * math.pi/N
    mx_ang = per_side * alpha
    beta = mx_ang/2
    #print(per_side, mx_ang)
    r = D/math.sin(beta)
    return r


def test(r):
    alpha = 2 * math.pi/N
    cnt = 0
    for i in range(1, N):
        dist = 2 * r * math.sin(i * alpha/2)
        #print("Checking dist", i, dist)
        if dist <= D2:
            cnt += 1
    return (cnt * N)//2

lo = 0
hi = 10**10
l = 10**30
for _ in range(60):
    mid = (lo + hi)/2

    cnt = test(mid)
    if cnt == T:
        l = min(l, mid)
        hi = mid
    elif cnt < T:
        hi = mid
    else:
        lo = mid
h = mx()
print(l, h)

