import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
coord = [nl() for _ in range(N)]
coord.sort()
if N%2 == 1:
    midx, midy = coord[N//2]
else:
    midx1, midy1 = coord[N//2 -1]
    midx2, midy2 = coord[N//2]
    midx = (midx1 + midx2)/2
    midy = (midy1 + midy2)/2

ylist = []
for x, y in coord:
    if x == midx:
        ylist.append(y)

import math
if len(ylist) == 0:
    #just split it in two
    L = 10**15
    x = math.floor(midx) - L
    print(x, 0)
    x2 = math.ceil(midx) + L
    print(x2, 0)
    exit()



py = - 10**15
point = int(midx) + 1, py
vec = -2, int(2 * (midy - py))

#print(vec)

dx = vec[1]
dy = -vec[0]

x1 = point[0] + dx
y1 = point[1] + dy

x2 = point[0] - dx
y2 = point[1] - dy

print(x1, y1)
print(x2, y2)

'''
def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 

p1 = x1, y1
p2 = x2, y2

double = 0
left = 0
right = 0

for p in coord:
    d1 = dist(p, p1)
    d2 = dist(p, p2)
    if d1 == d2:
        double += 1
        left += 1
        right += 1
    elif d1 < d2:
        left += 1
    else:
        right += 1
print(left, right, double)
'''



    