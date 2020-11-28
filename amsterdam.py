import heapq
import math

indata = raw_input().split()
M = int(indata[0])
N = int(indata[1])
R = float(indata[2])
ax, ay, bx,by = map(int, raw_input().split()) # segment nbr and then r


radDist = R/N
angDist = math.pi / M

#build graph!
def amsdist(s1, r1, s2,r2):
    return abs(r2 - r1) * radDist + abs(s2 - s1) * radDist * r2 * angDist

g = {}
dist = {}
INF = 10**12

for segment in range(M + 1):
    for halfring in range(N +1):
        g[(segment, halfring)] =[]
        dist[(segment, halfring)] = INF
for segment in range(M +1):
    for halfring in range(N +1):
        candidates = [(segment - 1, halfring), (segment + 1, halfring), (segment, halfring -1), (segment, halfring +1)]
        for seg, ring in candidates:
            if 0 <= seg <= M and 0 <= ring <= N:
                d = amsdist(segment,halfring,seg, ring)
                g[(segment, halfring)].append((d, (seg, ring)))
# Dijkstra from S to T

S = (ax,ay)
T = (bx,by)

pq = []
dist[S] = 0
pq.append((0, S))
heapq.heapify(pq)
done = False
while pq and not done:
    (nd, node) = heapq.heappop(pq)
    if node == T: done= True
    for (dd, nn) in g[node]:
        alt = dist[node] + dd
        if dist[nn] > alt:
            dist[nn] = alt
            heapq.heappush(pq, (dist[nn], nn))

s = '{}'.format(dist[T])
print(s)
