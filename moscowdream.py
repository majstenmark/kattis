import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]

a, b, c, n = nl()
if a >= 1 and b >= 1 and c >= 1 and n >= 3:
    if a + b + c >= n:
        print('YES')
        exit()
print('NO')