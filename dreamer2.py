from itertools import permutations 
from collections import Counter

MO = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MO2 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_digs(n):
    n1 = n%10
    n2 = n//10

    return [n2, n1]

def get_year_digits(m, d, c):
    li = get_digs(m) + get_digs(d)
    diff = Counter()

    for nbr in li:
        diff[nbr] -= 1
    y = []
    nbrs = []
    
    for nbr in range(0, 10):
        if c[nbr] + diff[nbr] > 0:
            for a in range( c[nbr] + diff[nbr]):
                nbrs.append(nbr)
    
    if len(nbrs) == 4:
        s = set()
        p = permutations(nbrs)
        for y in p:
            year = 1000 * y[0] + 100 * y[1] + 10 * y[2] + y[3]
            if year >=2000:
                s.add(year)
        return s
            
    return []


def all_days():
    days = []
    for mo in range(1, 13):
        for d in range(1, MO2[mo] + 1):
            days.append((mo, d))
    return days

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

days_in_year = all_days()

T = int(raw_input())
for t in range(T):
    digits = map(int, raw_input().replace(' ',''))
    c = Counter()
    for d in digits:
        c[d]+= 1
    
    cnt = 0
    mn = (INF, INF, INF)
    for m, d in days_in_year:
        year_digits = get_year_digits(m, d, c)
        for y in year_digits:
            if is_valid(d, m, y):
                    mn = min(mn, (y,m, d))
                    cnt += 1
    if cnt > 0:
        print('{} {:02d} {:02d} {}'.format(cnt, mn[2], mn[1], mn[0]))
    else:
        print(cnt)
    