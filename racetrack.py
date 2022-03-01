import sys
from collections import defaultdict as dd
from heapq import heappop as pop, heappush as push

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
racers = [nl() for _ in range(N)]
laps = [0] * N
laptimes = [t for t, _ in racers]
times = [0] * N
nexttime = []
li = dd(list)
for t in laptimes:
    push(nexttime, t)
for index, (t, l) in enumerate(racers):
    li[t].append(index)

mx = max(laptimes)

while len(nexttime) > 0:
    #print(nexttime)
    mn = pop(nexttime)
    
    players = li[mn]
    del li[mn]
    toadd = set()
    #players.sort()
    for p in players:
        laps[p] += 1
        if laps[p] == racers[p][1]:
            times[p] = mn
        else:
            worst = max(mn + racers[p][0], mx)
            li[worst].append(p)
            
            toadd.add(worst)
            #print('Added', mx)
    for t in toadd:
        if t != mx:
            push(nexttime, t)

    for t in toadd:
        mx = max(mx, t)
print('\n'.join(map(str, times)))

            




