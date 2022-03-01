import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def cnt(D, M, days):
    weekday = 0
    friday = 5
    c = 0
    for month in range(M):
        for d in range(days[month]):
            if weekday == 5 and d == 12:
                c += 1
            
            weekday += 1
            weekday %= 7
    return c

T = ni()
for _ in range(T):
    D, M = nl()
    days = nl()
    print(cnt(D, M, days))