import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

ROT = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def test(ins):
    dir = 0
    x, y = 0, 0
    for d in ins:
        if d == 'Right':
            dir += 1
            dir %= 4
        if d == 'Left':
            dir -= 1
            dir %= 4
        if d == 'Forward':
            dx, dy = ROT[dir]
            x += dx
            y += dy
    return (x, y) == (X, Y)



X, Y = nl()
N = ni()
ins = [inp() for _ in range(N)]
alt = ['Forward', 'Right', 'Left']
for i in range(N):
    orig = ins[i]
    for a in alt:
        if a != orig:
            ins[i] = a
            if test(ins):
                print(f'{i + 1} {a}')
                exit()
    ins[i] = orig
print('???')