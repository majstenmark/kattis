import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N, T = nl()
A, B, C, t0 = nl()
times = [t0]
for i in range(N-1):
    t = times[-1]
    ti = (A * t + B) % C + 1
    times.append(ti)
print(times)
times.sort()
currtime = 0
penalty = 0
solved = 0
MOD = 1000000007
for t in times:
    if currtime + t <= T:
        currtime += t
        penalty += currtime
        penalty %= MOD
        solved += 1

print(f'{solved} {penalty}')

