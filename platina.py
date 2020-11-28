import math
N = int(raw_input())
sq = 1
for n in range(N):
    sq *= 4
kv = math.sqrt(sq)
points = (kv +1) **2
print('{0:.0f}'.format(points))