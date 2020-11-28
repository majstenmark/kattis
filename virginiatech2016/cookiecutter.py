inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())
def nf(): return [float(v) for v in inp().split()]

def angle(p1, p2):
    return 0

def area(pts):
    su = 0.0
    for i in range(len(pts)):
        x, y = pts[i]
        u, v = pts[(i + 1)%len(pts)]
        su += x * v - u * y
    return 0.5 * abs(su)

def move(p, scale):
    return p[0] * scale, p[1] * scale

N = ni()
pts = [nf() for _ in range(N)]
A = ni()
startArea = area(pts)
scale2 = A/startArea
scale = scale2 ** 0.5
newPts = [move(p, scale) for p in pts]
minX = 10 ** 12
minY = 10 ** 12
for x, y in newPts:
    minX = min(minX, x)
    minY = min(minY, y)
for x, y in newPts:
    tx, ty = x - minX, y - minY
    print('{} {}'.format(tx, ty))

