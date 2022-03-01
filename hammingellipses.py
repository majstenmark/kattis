import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

Q, N, D = nl()
f1 = inp()
f2 = inp()

save = dd(int)
save[-1, 0] = 1
#save = [[0] * (D+1) for _ in range(N+1)]
#save[N][0] = 1

for n in range(N):
    for d in range(D+1):
        if f1[n] == f2[n]:
            same = save[n-1, d] 
            diff = (Q-1) * save[n-1, d-2]
        else:
            same = 2 * save[n-1, d-1] 
            diff = (Q-2) * save[n-1, d-2]
        res = same + diff
        save[n, d] += res

print(save[N-1, D])