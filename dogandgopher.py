import sys
indata = sys.stdin.read().strip().split('\n')
lines=(line for line in indata)
def dist(A, B):
    return ((A[0] - B[0]) ** 2 + (A[1] - B[1])** 2) ** 0.5

gx, gy, dx, dy = [float(x) for x in next(lines).split()]
G = gx, gy
D = dx, dy
holes=[]
while lines:
    line = next(lines, -1)
    if line == -1:
        break
    hx,hy = [float(x) for x in line.split()]
    holes.append((hx, hy))
for hole in holes:
    dg = dist(hole, G)
    dd = dist(hole, D)
    
    if dd > 2 * dg:
        #ok
        print('The gopher can escape through the hole at ({:.3f},{:.3f}).'.format(hole[0], hole[1]))
        exit()
print('The gopher cannot escape.')    