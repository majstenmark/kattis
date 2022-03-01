import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

T = ni()
for _ in range(T):
    N = ni()
    votes = [ni() for _ in range(N)]
    tot = sum(votes)
    mx = max(votes)
    ties = []
    for i in range(N):
        if votes[i] == mx:
            ties.append(i+1)
    if len(ties) == 1 and mx > tot/2:
        print(f'majority winner {ties[0]}')
    elif len(ties) == 1 and mx <= tot/2:
        print(f'minority winner {ties[0]}')
    else:
        print('no winner')
