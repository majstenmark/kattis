import sys
import math

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())


def vec(p1, p2):
    return p2[0]-p1[0], p2[1] - p1[1]

def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]

def scalar(u, v):
    return u[0] * v[0] + u[1] * v[1]

def magn(v):
    return math.hypot(v[0], v[1])

def angle(u, v):
    sc = scalar(u, v)
    m = magn(u) * magn(v)
    ang = math.acos(sc/m)
    return ang/math.pi * 180

def approx(x, y):
    return abs(x - y) < 0.00001

def isobs(p1, p2, p3):
    v1 = vec(p1, p2)
    v2 = vec(p1, p3)
    a1 = angle(v1, v2)

    u1 = vec(p2, p1)
    u2 = vec(p2, p3)
    b1 = angle(u1, u2)

    w1 = vec(p3, p1)
    w2 = vec(p3, p2)
    c1 = angle(w1, w2)
    
    if approx(a1, 90) or approx(b1, 90) or approx(c1, 90):
        return 'right'
    ang = max(a1, b1, c1)
    if ang > 90:
        return 'obtuse'
    
    return 'acute'

    




def isiso(p1, p2, p3):
    v1 = vec(p1, p2)
    v2 = vec(p1, p3)
    v3 = vec(p2, p3)
    l1 = magn(v1)
    l2 = magn(v2)
    l3 = magn(v3)
    li = [l1, l2, l3]
    li.sort()
    if approx(li[0], li[1]) or approx(li[1], li[2]):
        return 'isosceles'
    return 'scalene'
    

def istriangle(x1,y1,x2,y2,x3,y3):
    v1 = vec((x1,y1),(x2,y2))
    v2 = vec((x1,y1),(x3,y3))
    cr = cross(v1, v2)
    return cr != 0

N = ni()
for n in range(N):
    x1,y1,x2,y2,x3,y3 = nl()
    if istriangle(x1,y1,x2,y2,x3,y3):
        iso = isiso((x1,y1),(x2,y2),(x3,y3))
        obs = isobs((x1,y1),(x2,y2),(x3,y3))
        print(f'Case #{n+1}: {iso} {obs} triangle')
    else:
        print(f'Case #{n+1}: not a triangle')