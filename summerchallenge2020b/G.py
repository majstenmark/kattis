from heapq import heappop as pop, heappush as push
from collections import *

def nl():
    return [int(v) for v in raw_input().split()]
N = int(raw_input())
cities = [nl() for _ in range(N)]
Y0 = cities[0][0]
s = sorted(cities)
indeces = {v:k for k, (v, _, _) in enumerate(s)}
INF = 10**18
dist = defaultdict(lambda: INF)
dist[cities[0][0]] = 0
left = []
right = []
y, d, r = cities[0]
lo, hi = y  - d, y + d

lo_index = 0
hi_index = N-1

for index, (yi, di, ri) in enumerate(s):
    if yi <= lo:
        push(left, (abs(yi - y) + r + ri - yi, (yi, di, ri)))
        dist[yi] = abs(yi - y) + r
        lo_index += 1
    elif yi >= hi:
        push(right, (abs(yi - y) + r + ri + yi, (yi, di, ri)))
        dist[yi] = abs(yi - y) + r
        hi_index -= 1

def handleR(y1, r1, lo1, lo_index, do_push=True):
    pop(right)
    while 1:
        yi, di, ri = s[lo_index]
        if yi <= lo1:
            old = dist[yi]
            dist[yi] = min(old, dist[y1] + r1 + abs(y1 - yi))
            if dist[yi] < old and do_push:
                push(left, (dist[yi] + ri - yi, (yi, di, ri)))
            lo_index += 1
        else:
            break
    return lo_index

def handleL(y1, r1, hi2, hi_index, do_push=True):
    pop(left)
    while 1:
        yi, di, ri = s[hi_index]
        if yi >= hi2:
            old = dist[yi]
            dist[yi] = min(old, dist[y1] + r1 + abs(y1 - yi))
            if dist[yi] < old and do_push:
                push(right, (dist[yi] + ri + yi, (yi, di, ri)))
            hi_index -= 1
        else:
            break

    return hi_index

while 1:
    if not right and not left:
        break

    if right:
        c1, (y1, d1, r1) = right[0]
        lo1 = y1 - d1
    if left:
        c2, (y2, d2, r2) = left[0]
        hi2 = y2 + d2

    if not left:
        lo_index = handleR(y1, r1, lo1, lo_index)
    elif not right:
        hi_index = handleL(y2, r2, hi2, hi_index)
    else:
        if dist[y1] + r1 + abs(y1 - Y0) > dist[y2] + r2 + abs(y2 - Y0):
            hi_index = handleL(y2, r2, hi2, hi_index)
        else:
            lo_index = handleR(y1, r1, lo1, lo_index)

for y, _, _ in cities[1:]:
    if dist[y] == INF:
        print(-1)
    else:
        print(dist[y])
