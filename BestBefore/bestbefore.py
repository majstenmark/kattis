from itertools import permutations

cal = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6:30, 7:31, 8: 31, 9: 30, 10: 31, 11: 30, 12:31}

def isLeapYear(y):
    divBy4 = y % 4 == 0
    divBy100 = y % 100 == 0
    divBy400 = y % 400 == 0
    if divBy400:
        return True
    if divBy100:
        return False
    return divBy4

def okDays(y, m, d):
    maxDay = cal[m]
    if m == 2 and isLeapYear(y):
        maxDay = 29
    return 1 <= d <= maxDay

def okMonth(m):
    return 1 <= m <= 12

def fixYear(ys):
    if len(ys) == 4:
        return int(ys)
    y = int(ys)
    return 2000 + y if y < 100 else y


def checkObviouslyWrong(y, m, d):
    return y < 0 or y < 2000 or m < 1 or d < 1

def isLegal(y, m, d):
    if checkObviouslyWrong(y, m, d):
        return False
    return okMonth(m) and okDays(y, m, d)

def pad(y, m, d):
    ms = str(m)
    ms = ('0' if len(ms) == 1 else '') + ms
    ds = str(d)
    ds = ('0' if len(ds) == 1 else '') + ds
    return '{}-{}-{}'.format(y, ms, ds)

indata = raw_input()

data = indata.split('/')
perms = list(permutations(data))
legal = []
for ys, ms, ds in perms:
    y = fixYear(ys)
    m = int(ms)
    d = int(ds)
    if isLegal(y, m, d):
        legal.append(pad(y, m, d))

if len(legal) == 0:
    print indata, 'is illegal'
else:
    legal.sort()
    print legal[0]
