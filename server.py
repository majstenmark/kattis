import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N, T = nl()
tasks = nl()
time = 0
cnt = 0
for t in tasks:
    if t + time <= T:
        cnt += 1
        time += t
    else:
        break
print(cnt)