import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
states = [nl() for _ in range(N)]
undecided = []
decided_C = 0
decided_F = 0
tot_delegates = 0
for i in range(N):
    d, c, f, u = states[i]
    tot_delegates += d
    if c + u <= f:
        decided_F += d
    elif c > f + u:
        decided_C += d
    else:
        undecided.append((d, c, f, u))

majority = (tot_delegates + 2)//2
needed = majority - decided_C
if needed <= 0:
    print(0)
    exit()

def towin(state):
    d, c, f, u = state
    tot = c + f + u
    maj = (tot + 2)//2
    return maj - c

L = len(undecided)
INF = 10**30
cost = [[INF] * 2017 for _ in range(L+1)]
cost[0][0] = 0
for i in range(1, L + 1):
    d, c, f, u = undecided[i-1]
    for no_del in range(2017):
        cost_to_win = towin(undecided[i-1])
        #lose it
        cost[i][no_del] = cost[i-1][no_del]
        #win
        alt = cost_to_win + cost[i-1][no_del - d]
        cost[i][no_del] = min(cost[i][no_del], alt)

mn = INF

for no_del in range(needed, 2017):
    mn = min(cost[L][no_del], mn)
if mn < INF:
    print(mn)
else:
    print('impossible')