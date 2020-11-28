OUT = 'out'
IN = 'in'
ON = 'on'
DEBUG = False
def dprint(s):
    if DEBUG:
        print(s)

def vec(P1, P2):
    return [P2[0] -P1[0],P2[1] - P1[1]]

def crossZsign(v1, v2):
    if v1[0] * v2[1] - v2[0]*v1[1] > 0:
        return 1
    if v1[0] * v2[1] - v2[0]*v1[1] == 0:
        return 0
    return -1

def lineeq(p, q):
    return (-q[1] + p[1],
        q[0] - p[0],
        p[0]*q[1] - p[1]*q[0])


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
        x = Dx / D
        y = Dy / D
        return x,y, True
    else:
        return 0, 0, False

def dist2(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def closeBy(p, s1, s2):
    sDist = dist2(s1, s2)
    ps1 = dist2(p, s1)
    ps2 = dist2(p, s2)
    return ps1 <= sDist and ps2 <= sDist

def onseg(p, seg):
    v1 = vec(seg[0], p)
    v2 = vec(seg[0], seg[1])
    sign = crossZsign(v1, v2)
    return sign == 0 and closeBy(p, seg[0], seg[1])

def isIntersecting(p, seg, pline, segLine):

    infinity = (p[0] + 1, p[1] + 100000)
    x, y, intersects = intersection(pline, segLine)
    if intersects:
        segV = vec(seg[0], seg[1])
        vp = vec(seg[0], p)
        vinf = vec(seg[0], infinity)

        ps1 = vec(p, seg[0])
        ps2 = vec(p, seg[1])
        pinf = vec(p, infinity)

        sign1 = crossZsign(segV, vp)
        sign2 = crossZsign(segV, vinf)
        sign3 = crossZsign(ps1, pinf)
        sign4 = crossZsign(ps2, pinf)

        if sign1 == -sign2 and sign3 == -sign4:
            return True
    return False

def onpoly(p, poly):
    for seg, segLine in poly:
        if onseg(p, seg):
            return True
    return False

def inpoly(p, poly):
    if onpoly(p, poly):
        return ON

    infinity = (p[0] + 1, p[1] + 100000)
    pline = line(infinity, p)
    count = 0
    for seg, segLine in poly:
        if isIntersecting(p, seg, pline, segLine):
            count += 1
    dprint(count)
    if count % 2 == 1:
        return IN
    return OUT

N =int(raw_input())

while N != 0:
    poly = []
    points = []
    for n in range(N):
        x, y = map(int, raw_input().split())
        points.append((x, y))
    for index in range(N):
        seg = (points[index], points[(index + 1)% N])
        segLine = line(seg[0], seg[1])
        poly.append((seg, segLine))
    M = int(raw_input())
    for m in range(M):
        x, y = map(int, raw_input().split())
        print(inpoly((x,y), poly))
    N =int(raw_input())
