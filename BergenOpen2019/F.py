def nl():
    return [int(v) for v in raw_input().split()]
def ni():
    return int(raw_input())

def test(ang, W):
    W = float(W)
    cnt = 0
    h = math.tan(ang) * W/2
   
    for i in range(K-1):
        ang2 = math.atan(2 * math.tan(ang))
        h2 = h + math.tan(ang2) * W
        ang = ang2
        h = h2
    ang2 = math.atan(2 * math.tan(ang))
    h2 = h + math.tan(ang2) * W/2
    h = h2
    return h < L
    

import math
K, W, L = nl()
lo = 0.0
hi = math.pi/2
for i in range(100):
    mid = (lo + hi)/2
    if test(mid, W):
        lo = mid
    else:
        hi = mid
print(lo*180/math.pi)


