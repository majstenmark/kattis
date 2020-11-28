R, C = map(int, raw_input().split())
room = [raw_input() for _ in range(R)]
top = [[0]*C for _ in range(R)]
for c in range(C):
    t = 0
    for r in range(R):
        if room[r][c] == '.':
            t += 1
            top[r][c] = t
        else:
            t = 0

def opt(row, lo, hi):
    mid =  (lo + hi)/2

    #print 'row', row, 'lo', lo, 'hi', hi, 'mid', mid
    if lo >= hi:
        return top[row][mid] + 1
    left, right = mid, mid
    best = top[row][mid] + 1
    minH = top[row][mid]
    while left > lo and right < hi:
        ln = left -1
        rn = right +1
        if top[row][ln] > top[row][rn]:
            minH = min(minH, top[row][ln])
            left = ln
            best = max(best, minH + (right - left + 1))
        else:
            minH = min(minH, top[row][rn])
            right = rn
            best = max(best, minH + (right - left + 1))
    while left > lo:
        ln = left -1
        minH = min(minH, top[row][ln])
        left = ln
        best = max(best, minH + (right - left + 1))
    while right < hi:
        rn = right + 1
        minH = min(minH, top[row][rn])
        right = rn
        best = max(best, minH + (right - left + 1))
    return max(best, max(opt(row, lo, mid -1), opt(row, mid+1, hi)))

MAX = 0
for r in range(R):
    first = -1
    second = -1
    for c in range(C):
        if room[r][c] == '.':
            if first == -1:
                first = c
        else:
            if first != -1:
                second = c -1
                MAX = max(MAX, opt(r, first, second))
            first = -1
    if first != -1:
        MAX = max(MAX, opt(r, first, C-1))

print MAX * 2 -1
