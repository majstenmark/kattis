from math import cos, sin, pi

def parse(line):
    data = line.split()
    x = float(data[0])
    y = float(data[1])
    startdir = float(data[3])
    ins = []
    for i in range(4, len(data), 2):
        ins.append((data[i], float(data[i+1])))
    return x, y, startdir, ins
    
def walk(x, y, currdir, ins):
    d = currdir/180 * pi
    for cmd, val in ins:
        if cmd == 'walk':
            dx = val * cos(d)
            dy = val * sin(d)
            x += dx
            y += dy
        if cmd == 'turn':
            d += (val/180 * pi)
    return x, y

def dist(avx, avy, x, y):
    return ((avx - x) **2 + (avy - y) ** 2) ** 0.5

N = int(input())
while N != 0:
    avx, avy = 0, 0
    endpos = []
    for _ in range(N):
        x, y, d, ins = parse(input())
        endx, endy = walk(x, y, d, ins)
        #print(endx, endy)
        endpos.append((endx, endy))
        avx += endx
        avy += endy
    avx /= N
    avy /= N
    mxdist = 0
    for x, y in endpos:
        d = dist(avx, avy, x, y)
        mxdist = max(mxdist, d)
    print(f'{avx} {avy} {mxdist}')
    N = int(input())
        