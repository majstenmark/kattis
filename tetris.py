import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

p1 = [[], [0, 0, 0]]
p2 = [[0]]
p3 = [[0, 1], [-1]]
p4 = [[-1, 0], [1]]
p5 = [[0, 0], [1], [-1], [-1, 1]]
p6 = [[0, 0], [0], [1, 0], [-2]]
p7 = [[0, 0], [0], [2], [0, -1]]
pieces = [p1, p2, p3, p4, p5, p6, p7]
C, P = nl()
H = nl()
ways = pieces[P-1]
cnt = 0

def ok(diff, H, pos):
    L = len(diff)
    diff2 = []
    h = H[pos]
    for l in range(L):
        if pos + l + 1< len(H):
            h2 = H[pos + l + 1]
            diff2.append(h2 - h)
            h = h2
    return diff == diff2

for pos in range(C):
    for diff in ways:
        if ok(diff, H, pos):
            cnt += 1
print(cnt)
    