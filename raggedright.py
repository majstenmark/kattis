import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

lines = [line.strip() for line in sys.stdin.readlines()]

n = 0
for line in lines:
    n = max(len(line), n)

penalty = 0
for line in lines[0:-1]:
    L = len(line)
    penalty += (n - L) ** 2
print(penalty)
