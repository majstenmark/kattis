from collections import defaultdict as dd

points = [map(int, raw_input().split()) for _ in range(3)]
xcoords = dd(int)
ycoords = dd(int)
for x, y in points:
    xcoords[x] += 1
    ycoords[y] += 1
xcnt = [(c, v) for v, c in xcoords.items()]
ycnt = [(c, v) for v, c in ycoords.items()]
xcnt.sort()
ycnt.sort()
print('{} {}'.format(xcnt[0][1], ycnt[0][1]))