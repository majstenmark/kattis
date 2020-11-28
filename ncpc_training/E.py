from collections import *
import sys
sys.setrecursionlimit(10000)
inp = input
def ni(): return int(inp())
def nl(): return [int(v) for v in inp().split()]

def getYMD(s):
    return int(s[:4]), int(s[4:6]), int(s[6:8])
startDate = getYMD(inp())
events = []
events.append((startDate, 0))
for line in sys.stdin:
    d, no = line.split()
    events.append((getYMD(d), int(no)))

dem = 0
mer = 0
out = []
out.append((startDate, 0, 0))
cY, cM, cD = startDate
for (nY, nM, nD), d in events:
    cnt = 0
    cY += 1
    while (cY, cM, cD) <= (nY, nM, nD):
        if dem == 0:
            cnt += 1
        if dem == 0 and cnt%2 == 0:
            mer = min(5, mer + 1)
        dem = max(0, min(dem - 2, dem//2))
        out.append(((cY, cM, cD), mer, dem))
        cY += 1
    red = min(mer, (d+1)//2)
    d = max(0, d - 2*red)
    mer -= red
    dem += d
    cY, cM, cD = (nY, nM, nD)
    out.append(((cY, cM, cD), mer, dem))

cY += 1
cnt = 0
while mer < 5:
    if dem == 0:
        cnt += 1
    if dem == 0 and cnt%2 == 0:
        mer = min(5, mer + 1)
    dem = max(0, min(dem - 2, dem//2))
    out.append(((cY, cM, cD), mer, dem))
    cY += 1

last = -1, -1
V = []
for T, mer, dem in out:
    if (mer, dem) != last:
        V.append((T, mer, dem))
        last = mer, dem

for (y, m, d), mer, dem in V:
    dstr = '{}-{:02d}-{:02d}'.format(y, m, d)
    if mer == dem == 0:
        print(dstr, 'No merit or demerit points.')
    elif mer > dem:
        print(dstr, '{} merit point(s).'.format(mer))
    else:
        print(dstr, '{} demerit point(s).'.format(dem))



