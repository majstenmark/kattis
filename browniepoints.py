N  = int(raw_input())
while N > 0:
    points = []
    for n in range(N):
        x, y = [int(v) for v in raw_input().split()]
        points.append((x, y))
    cx, cy = points[N/2]
    lefttop = 0
    leftbtn =0
    righttop = 0
    rightbtn = 0
    for x, y in points:
        if x < cx and y < cy:
            leftbtn += 1
        if x < cx and y > cy:
            lefttop += 1
        if x > cx and y < cy:
            rightbtn += 1
        if x > cx and y > cy:
            righttop += 1
    olli = lefttop + rightbtn
    stan = righttop + leftbtn
    print('{} {}'.format(stan, olli))
    N  = int(raw_input())
    