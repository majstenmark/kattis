import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N, M = nl()
edges = [nl() for _ in range(M)]
T = N-1
adj = [[] for _ in range(N)]
for k, l in edges:
    if k != T: adj[k].append(l)
    if l != T: adj[l].append(k)

def move(prob):
    nxt = [0] * N
    for i in range(T):
        p = 1/len(adj[i])
        for o in adj[i]:
            nxt[o] += p * prob[i]
    return nxt

prob = [0] * N
prob[0] = 1.
thres = 10**-10
tot = 1.
exp = 0
steps = 0
while tot > thres:
    prob = move(prob)
    steps += 1
    exp += prob[T] * steps

    tot = 0
    for i in range(T):
        tot += prob[i]
    
    #print(f'Step {steps} tot {tot} prob {prob}')
    
print(exp)