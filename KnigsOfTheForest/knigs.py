from heapq import heappop as pop
from heapq import heappush as push


K, N = map(int, raw_input().split())
Ky,Kp = map(int, raw_input().split())
pool = []
future = [(0, 0)for _ in range(N+K-2)]
if Ky == 2011:
    push(pool, (-Kp, -1))
else:
    future[Ky-2012] = (-Kp, -1)

for moose in range(N + K - 2):

    y, p = map(int, raw_input().split())
    if y == 2011:
        push(pool, (-p, moose))
    else:
        future[y-2012] = (-p, moose)
for year in range(N):
    p, alpha = pop(pool)
    if alpha == -1:
        print year + 2011
        exit()
    push(pool, future[year])

print 'unknown'
