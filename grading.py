import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

A, B, C, D, E = nl()
grades = [('A', A), ('B', B), ('C', C), ('D', D), ('E', E)]
score = ni()
for lt, pt in grades:
    if score >= pt:
        print(lt)
        exit()
print('F')