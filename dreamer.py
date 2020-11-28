from itertools import permutations 

MO = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(y):
    if y % 400== 0:
        return True
    if y % 100 == 0 and not y % 400 == 0:
        return False
    if y % 4 == 0 and not y % 100 == 0:
        return True
    return False


def is_valid(d, m, y):
    if y < 2000:
        return False
    leap = is_leap(y)
    if leap and m == 2 and d == 29:
        return True
    if 1 <= m <= 12:
        mx = MO[m]
        if 1 <= d <= mx:
            return True
    return False


INF = 100000

T = int(raw_input())
for t in range(T):
    digits = list(raw_input().replace(' ',''))
    cnt = 0
    mn = (INF, INF, INF)
    li = []
    perms = permutations(digits)
    seen = set()
    for p in perms:
        d = int(''.join(p[0:2]))
        m = int(''.join(p[2:4]))
        y = int(''.join(p[4:]))
        if (y, m, d) not in seen:
            seen.add((y, m, d))
            if is_valid(d, m, y):
                mn = min(mn, (y,m, d))

                cnt += 1
    for y, m, d in li:
        print('{} {:02d} {:02d}'.format(y, m, d))
    if cnt > 0:
        print('{} {:02d} {:02d} {}'.format(cnt, mn[2], mn[1], mn[0]))
    else:
        print(cnt)
    