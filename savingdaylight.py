import sys
for line in sys.stdin.readlines():
    data = line.split()
    date = data[:3]
    h, m = map(int, data[3].split(':'))
    hh, mm = map(int, data[4].split(':'))
    min1 = h * 60 + m
    min2 = hh * 60 + mm
    diff = min2 - min1
    hr = diff // 60
    mr = diff % 60
    out = '{} {} hours {} minutes'.format(' '.join(date), hr, mr)
    print(out)