import sys

def check(li, w, mx):
    start = 0.0
    end = 0.0
    for l in li:
        start = l - w
        #print('{} {} {}'.format(l, start, end))
        if start > end:
            return False
        end = l + w
    return end >= mx


data = sys.stdin.readlines()
for t in range(0, len(data) -1, 3):
    line = (data[t].strip()).split()
    nx = int(line[0])
    ny = int(line[1])
    w = float(line[2])/2.0

    hlines = [float(v) for v in data[t+1].strip().split()]
    vlines = [float(v) for v in data[t+2].strip().split()]
    hlines.sort()
    vlines.sort()
    if check(hlines, w, 75) and check(vlines, w, 100):
        print('YES')
    else:
        print('NO')

