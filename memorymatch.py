import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
K = ni()
moves = []
picked = 0
cnt = dd(set)

for _ in range(K):
    data = inp().split()
    c1 = int(data[0])
    c2 = int(data[1])
    p1 = data[2]
    p2 = data[3]
    if p1 == p2:
        picked += 1
    cnt[p1].add(c1)
    cnt[p2].add(c2)
can_pick =0
seen = set()
unpaired = 0
for cat in cnt.keys():
    pos = cnt[cat]
    seen |= pos
    if len(pos) == 2:
        can_pick += 1
    else:
        unpaired += 1

left = N - len(seen)
to_pick = can_pick - picked

if unpaired == 0 and left == 2:
    to_pick += 1
if unpaired ==left:
    to_pick += left
print(to_pick)
