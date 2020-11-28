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

N, M = nl()

amount = nl()

G = [[] for _ in range(N)]
PCount = [0]*N

for _ in range(M):
    u, v, w = nl()
    G[v].append((u, w))
    PCount[u] += 1

Q = []
for i, c in enumerate(PCount):
    if c == 0: Q.append(i)

while Q:
    Q2 = []
    for v in Q:
        for u, w in G[v]:
            amount[u] += amount[v]*w
            PCount[u] -= 1
            if PCount[u] == 0:
                Q2.append(u)
    Q = Q2
print(' '.join(map(str, amount)))
