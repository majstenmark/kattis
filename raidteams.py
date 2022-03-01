import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
adv = []
for _ in range(N):
    line = inp().split()
    skills = [int(v) for v in line[1:]]
    adv.append((line[0], skills))

skill1 = sorted(adv, key = lambda x: (-x[1][0], x[0]))[::-1]
skill2 = sorted(adv, key = lambda x: (-x[1][1], x[0]))[::-1]
skill3 = sorted(adv, key = lambda x: (-x[1][2], x[0]))[::-1]
teams = []
used = set()

while len(skill1) > 0 and len(skill2) > 0 and len(skill3) > 0:
    def pick(li):
        while len(li) > 0 and li[-1][0] in used:
            li.pop()
        if len(li) > 0:
            pl, v = li.pop()
            used.add(pl)
            return pl
        return None

    pl1 = pick(skill1)   
    pl2 = pick(skill2)
    pl3 = pick(skill3)
    if pl1 != None and pl2 != None and pl3 != None:
        names = [pl1, pl2, pl3]
        names.sort()
        pl1, pl2, pl3 = names
        teams.append(pl1 + ' ' +  pl2 + ' '+  pl3)
     
print('\n'.join(teams))
        
