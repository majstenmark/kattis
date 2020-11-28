import math

TIME = 10
DIST = 5
MAXN = 20

world = None
deadmoles = None

n = MAXN


def _ball(d, x,y):
    positions = []
    for x_ in range(x - d, x + d + 1):
        for y_ in range(y - d, y + d + 1):
            if (x - x_)**2 + (y - y_)**2 > d*d:
                continue
            positions.append((x_,y_))
    return positions

deltas = [
        _ball(d, 0,0) for d in range(6)
        ]

def ball(d,x,y):
    return [(x + dx, y + dy) for (dx, dy) in deltas[d]]

PANIC = DIST + 1

def init():
    global world, deadmoles
    world = [
                [
                    [False] * (n + 2 * PANIC)
                    for _ in range(n + 2 * PANIC)
                ]
            for _ in range(TIME + 1)]

    deadmoles = [
                [
            [0] * (n + 2 * PANIC)
            for _ in range(n + 2 * PANIC)
            ]
        for _ in range(TIME + 1)]
    for x in range(n + 2 * PANIC):
        for y in range(n + 2 * PANIC):
            deadmoles[0][x][y] = 0

def set(x, y, t):
    global world
    world[t][x + PANIC][y + PANIC] = True


def gcd(a, b): return gcd(b, a%b) if b else a

def intcoordsbetween(x,y,x_,y_):
    w = abs(x_ - x)
    h = abs(y_ - y)
    div = gcd(h,w)
    signx = -1 if x_ < x else 1
    signy = -1 if y_ < y else 1
    res = [(x,y)]
    x__, y__ = x, y
    while x__ != x_ or y__ != y_:
        x__ = x__ + signx * (w // div)
        y__ = y__ + signy * (h // div)
        res.append((x__,y__))
    return res


def count_moles(t, x, y, x_, y_):
    total = 0
    for x__, y__ in intcoordsbetween(x, y, x_, y_):
        total += world[t][x__][y__]
    return total

def solve(d):
    global deadmoles
    DIM = n + 2 * PANIC
    for t in range(1, TIME + 1):
        for x in range(DIM):
            for y in range(DIM):
                for x_, y_ in ball(d,x,y):
                    if x_ < 0 or y_ < 0 or x_ >= DIM or y_ >= DIM:
                        continue
                    damage = count_moles(t, x,y, x_, y_)
                    old = deadmoles[t - 1][x][y]
                    deadmoles[t][x_][y_] = max(deadmoles[t][x_][y_], damage + old)
    res = -1
    for x in range(DIM):
        for y in range(DIM):
            damagehere = deadmoles[10][x][y]
            #assert damagehere is not None
            res = max(res, damagehere)
    return res

try: inp = raw_input
except: inp = input

while True:
    n, d, m = map(int, inp().split())
    if n == d == m == 0:
        break
    init()
    for _ in range(m):
        x, y, t = map(int, inp().split())
        set(x, y, t)
    #print ("!", count_moles(1,TIME*DIST,TIME*DIST,TIME*DIST,TIME*DIST))
    print(solve(d))
