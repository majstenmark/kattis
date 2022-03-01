import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N, K = nl()

exp = 0
p = 1/N
#last roll
for i in range(1, N+1):
    exp += p * i

for k in range(1, K):
    
    reroll = int(exp)
    stay = (reroll + 1 + N) * (N - reroll)/2
    p_stay = stay * p
    p_reroll = reroll * p
    exp = p_reroll * exp + p_stay

print(exp)






