def readdata():
    (b, h) = map(int, input().split())
    rect = []
    while b !=-1 and h != -1:
        rect += [(b, h)]
        (b, h) = map(int, input().split())
    return rect

def solve(m, rect):
    maxW = 0
    totH = 0
    currH = 0
    currW = 0
    for (b, h) in rect:

        if currW + b <= m:
            currW += b
            currH = max(currH, h)
        else:
            maxW = max(maxW, currW)
            currW = b
            totH += currH
            currH = h
    maxW = max(maxW, currW)
    totH += currH


    return (maxW, totH)

m = int(input())
while m > 0:
    rect = readdata()
    res = solve(m, rect)
    print(res[0], 'x', res[1])
    m = int(input())
