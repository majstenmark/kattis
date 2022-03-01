import sys
from collections import defaultdict as dd
itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def ni(): return int(inp())

N = ni()
socks = dd(lambda: [0, 0, 0])
for _ in range(N):
    data = inp().split()
    t, side, _ = data
    no = int(data[-1])
    if side == 'any':
        socks[t][0] += no
    if side == 'left':
        socks[t][1] += no
    if side == 'right':
        socks[t][2] += no

#check impossible first
def isimpossible():
    
    for cat, li in socks.items():
        cnt = 0
        for i in li:
            if i > 0:
                cnt += 1
        if cnt >= 2 or li[0] >= 2:
            return False
    return True

if isimpossible():
    print('impossible')
    exit()
        

worst = 0
for cat, li in socks.items():
    oneside = max(li[1], li[2])
    if oneside == 0:
        worst += 1
    else:
        worst += oneside
print(worst +1)
    

        

