import sys
from collections import defaultdict as dd, Counter
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
subsets = [ni() for _ in range(2**N)]
subsets.sort()


if subsets[0] != 0:
    print('impossible')
    exit()

elems = []
ws = []
torem = Counter()
for w in subsets[1:]:
    if len(elems) > N:
        print('impossible')
        exit()
    
    if torem[w] == 0:
        elems.append(w)
    
        for s in list(ws):
            torem[s + w] += 1
            ws.append(s+w)
        ws.append(w)
    else:
        torem[w] -= 1
    
if sum(torem.values()) == 0:
    #ok
    s = '\n'.join(map(str, elems))
    print(s)
else:
    print('impossible')