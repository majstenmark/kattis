import math
from collections import namedtuple
Point = namedtuple('Point', 'x y id')
INF = 10**12
dummy  = Point(0, 0, -1)
def dist2(p1, p2):
    d1 = p1.x - p2.x
    d2 = p1.y - p2.y
    return d1 **2 + d2 **2

def brute(xlist):
    delta = INF
    P1, P2 = dummy, dummy
    for p in range(len(xlist) -1):
        for q in range(p+1, len(xlist)):
            p1 = xlist[p]
            p2 = xlist[q]
            d2 = dist2(p1, p2)
            if d2 < delta:
                delta = d2

        #        print 'updating '
                P1, P2 = p1, p2
    return delta, P1, P2

def DoC(xlist):
    if len(xlist) < 50:
        return brute(xlist)
    mid = len(xlist)/2
    xllist = xlist[0:mid]
    xrlist = xlist[mid:len(xlist)]

    deltaL, p1L, p2L = DoC(xllist)
    delta, p1, p2 = DoC(xrlist)
    if deltaL < delta:
        delta = deltaL
        p1, p2 = p1L, p2L

    line = xlist[mid].x
    ylist = []
    linedist = math.sqrt(delta)
    for p in xlist:
        if abs(p.x - line) < linedist:
            ylist.append(p)

    ylist.sort(key = lambda v: v.y)


    for p in range(len(ylist)):
        for i in range(p+1, min(p+8, len(ylist))):
#            print 'comparing ', ylist[p], ylist[i]
            d2 = dist2(ylist[p], ylist[i])
#            print 'd2', d2
            if d2 < delta:
                delta = d2

        #        print 'updating '
                p1, p2 = ylist[p], ylist[i]

    return delta, p1, p2

N = int(raw_input())
while N != 0:
    points = []
    for p in range(N):
        x, y = map(float, raw_input().split())
        points.append(Point(x, y, p))

    xsort = sorted(points, key= lambda v: v[0])
    minDist2, p1, p2 = DoC(xsort)
    print '{:.2f} {:.2f} {:.2f} {:.2f}'.format(p1.x, p1.y, p2.x, p2.y)
    N = int(raw_input())
