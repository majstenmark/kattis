import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def test(curr, target, a):
    presses = 1
    overlap = 0
    for i in range(min(len(target), len(a))):
        if target[i] != a[i]:   
            break
        overlap = i+1
    #print('overlapping', overlap)
    todel = len(a) - overlap
    #print('todel', todel)
    
    presses += todel
    toadd = len(target) - overlap
    #print('toadd', toadd)
    
    presses += toadd
    return presses



T = ni()
for _ in range(T):
    target = inp()
    curr = inp()
    alt = [inp() for _ in range(3)]
    #print("JUST TYPE")
    best = test(curr, target, curr) -1
    #print(best)

    for a in alt:
        #print('TEST ', a)
        t = test(curr, target, a)
        best = min(best, t)
        #print(a, t)
    print(best)