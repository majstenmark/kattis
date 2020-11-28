from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s):
    sys.stderr.write('{}\n'.format(s))

def ni():
    return int(inp())

def nl():
    return [int(_) for _ in inp().split()]

N = ni()
P = [nl() for _ in range(N)]

SC = 0

from heapq import *


D = defaultdict(list)

M = max(P)[0]

for t, d in P:
    D[t].append(d)

pq = []
for t in range(M, 0, -1):
    for d in D[t]:
        heappush(pq, -d)
    if pq:
        SC += -heappop(pq)
print(SC)
