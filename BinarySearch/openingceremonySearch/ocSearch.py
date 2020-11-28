from collections import deque
N=int(raw_input())
hs=[int(v) for v in raw_input().split()]

hs.sort(key=lambda x: -x)
INF = 10**12
best = N # only vertical shots

for v in range(N):
    best = min(best, v + hs[v])

print(best)
