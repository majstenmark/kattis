
def vec(P1, P2):
    return [P2[0] -P1[0],P2[1] - P1[1]]

def crossZsign(v1, v2):
    if v1[0] * v2[1] - v2[0]*v1[1] > 0:
        return 1
    if v1[0] * v2[1] - v2[0]*v1[1] == 0:
        return 0
    return -1

def onseg(p, seg):
    v1 = vec(seg[0], p)
    v2 = vec(seg[0], seg[1])
    sign = crossZsign(v1, v2)
    return sign == 0 and closeBy(p, seg[0], seg[1])

def dist2(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def closeBy(p, s1, s2):
    sDist = dist2(s1, s2)
    ps1 = dist2(p, s1)
    ps2 = dist2(p, s2)
    return ps1 <= sDist and ps2 <= sDist

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx * 1.0/ D
        y = Dy * 1.0/ D
        return x,y, True
    else:
        return 0, 0, False

def isColinear(p1, p2, p3, p4):
    v1 = vec(p1, p2)
    v2 = vec(p1, p3)
    v3 = vec(p3, p4)
    sign = crossZsign(v1, v2)
    sign2 = crossZsign(v2, v3)
    return sign == 0 and sign2 == 0

def isOverlapping(p1, p2, p3, p4):
    #print 'p1', p1
    x1, x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
    x3, x4 = min(p3[0], p4[0]), max(p3[0], p4[0])
    y1, y2 = min(p1[1], p2[1]), max(p1[1], p2[1])
    y3, y4 = min(p3[1], p4[1]), max(p3[1], p4[1])
    test1 = x1 <= x4 and x2 >= x3
    test2 = y1 <= y4 and y2 >= y3
    overlap = test1 and test2
    if overlap:
        li = [p1, p2, p3, p4]
        li.sort()
        pl = li[1]
        ph = li[2]
        if pl != ph:
            return pl, ph, TWOPOINTS
        return pl, ph, ONEPOINT
    return p1, p2, NOPOINT


TWOPOINTS = 2
ONEPOINT = 1
NOPOINT = 0

N = int(raw_input())
for n in range(N):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, raw_input().split())
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    p4 = (x4, y4)
    L1 = line(p1, p2)
    L2 = line(p3, p4)
    x, y, intersecting = intersection(L1, L2)
    if intersecting:
        #print 'intersecting', x, y
        #print L1
        #print L2
        if closeBy((x, y), p1, p2) and closeBy((x, y), p3, p4):
        #    print 'intersecting', x, y
            #print L1
            #print L2
            print('{:.2f} {:.2f}'.format(x, y))
        else:
            print('none')
    elif isColinear(p1, p2, p3, p4):
        pl, ph, overlapping = isOverlapping(p1, p2, p3, p4)
        if overlapping == TWOPOINTS:
            #print 'towpoints'
            s1 = '{:.2f} {:.2f}'.format(pl[0], pl[1])
            s2 = '{:.2f} {:.2f}'.format(ph[0], ph[1])
            print('{} {}'.format(s1, s2))
        elif overlapping == ONEPOINT:
            #print 'one point'
            s = '{:.2f} {:.2f}'.format(pl[0],pl[1])
            print(s)
        else:
            print('none')
    else:
        print('none')
