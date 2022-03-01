import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())


N = ni()
grid = [nl() for _ in range(N)]
bits = [[0] * 30 for _ in range(N)]
for i in range(N):
    for c in range(N):
        if i != c:
            val = grid[i][c]
            b = bin(val)[2:]
            for index, value in enumerate(b[::-1]):
                if value == '1':
                    bits[i][index] = 1
out = []
for i in range(N):
    binary = ''.join(map(str, bits[i][::-1]))
    intval = int(binary, 2)
    out.append(str(intval))
print(' '.join(out))
