import sys
from collections import defaultdict as dd, Counter
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N, T = nl()
A, B, C, t0 = nl()
times = [t0]
seen = {t0: 0}
cycle_start = -1
for i in range(1, N):
    t = times[-1]
    ti = (A * t + B) % C + 1
    
    if ti in seen:
        cycle_start = seen[ti]
        break
    times.append(ti)
    seen[ti] = i

no_seen = len(seen)

cnt = Counter()

if cycle_start > -1:

    for i in range(0, cycle_start):
        val = times[i]
        cnt[val] += 1
    cycle_len = len(times) - cycle_start

    #print(f'cyclestart {cycle_start} cyclelen {cycle_len}')
    left = N - cycle_start
    no_cycles = left//cycle_len
    last = left % cycle_len
    #print(f'no cycles {no_cycles} left {left}, last {last}, len times {len(times)}')
    for i in range(cycle_start, len(times)):
        val = times[i]
        cnt[val] += no_cycles
        if last > 0 and i < cycle_start + last:
            cnt[val] += 1
else:
    for i in range(0, len(times)):
        val = times[i]
        cnt[val] += 1
    
#print(cnt)
items = list(cnt.items())
items.sort()
solved = 0
penalty = 0
currtime = 0

def calc(t, c, currtime):
    to_add = (1 + c) * c//2
    return currtime * c + t * to_add

MOD = 1000000007

for t, c in items:
    
    if currtime + t * c <= T:
        k = c
    else:
        k = (T - currtime) //t

    tot = calc(t, k, currtime)

    currtime += t*k
    solved += k
    penalty += tot
    penalty %= MOD

   
print(f'{solved} {penalty}')

