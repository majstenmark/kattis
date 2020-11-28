import sys
from collections import defaultdict as dd
itr = (line for line in sys.stdin.read().split('\n'))

N = int(next(itr))
lifts = dd(list)
yset= set()
for n in range(N):
    x, y, t = map(int, next(itr).split())
    if len(lifts[y]) == 0:
        lifts[y] = [0,0, 0]
    lifts[y][t-1] += 1
    yset.add(y)

ys = list(yset)
ys.sort()
seg_cnt = 0

for y in ys[:-1]:
    t1, t2, paired1 = lifts[y]
    #print(lifts[y])
    if len(lifts[y+1]) > 0:
        nt1, nt2, _ = lifts[y+1]
        #first pair the twos in next
        cand_lvl = t1 + t2 - paired1
        #print(cand_lvl, y)
        p2 = min(cand_lvl, nt2)
        cand_lvl -= p2
        seg_cnt += p2

        # then pair singles
        p1 = min(cand_lvl, nt1)
        seg_cnt += p1
        lifts[y+1][2] += p1
        #print('paired p2 = {}, p1 = {} level= {}'.format(p2, p1, y))
        

print(seg_cnt)
            
