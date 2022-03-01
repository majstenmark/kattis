import sys
from collections import defaultdict as dd, deque
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N, M = nl()
workers = [nl() for _ in range(N)]
events = []
for i, (a, s) in enumerate(workers):
    events.append((a, 'B', i))
    events.append((a+ s, 'A', i))
events.sort()
saved = 0
unlocked = deque()

def free(unlocked, time):
    while unlocked:
        first = unlocked.popleft()
        if first + M >= time:
            return True
    return False

for time, eventtype, id in events:
    if eventtype == 'B':
        if free(unlocked, time):
            saved += 1
            #print('saved')
    else:
        unlocked.append(time)
print(saved)

    