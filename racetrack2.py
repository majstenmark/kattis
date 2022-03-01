import sys
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

for i, t in enumerate(laptimes):
    push(nexttime, (t, i))

mx = max(laptimes)

while len(nexttime) > 0:
    #print(nexttime)
    mn, p = pop(nexttime)

    #players.sort()
    laps[p] += 1
    if laps[p] == racers[p][1]:
        times[p] = mn
    else:
        worst = max(mn + racers[p][0], mx)
        push(nexttime, (worst, p))
        mx = max(mx, worst)

print('\n'.join(map(str, times)))

            




