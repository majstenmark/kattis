import sys
from collections import defaultdict as dd

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def solve(N, office, empl):
    towns = dd(list)
    for town, cap in empl:
        towns[town].append(cap)
    cars = [0] * (N + 1)
    for town, li in towns.items():
        if town != office:
            ppl = len(li)
            li.sort(reverse = True)
            ppl_in_cars = 0
            i = 0
            while ppl_in_cars < ppl and i < len(li):
                ppl_in_cars += li[i]
                i += 1
            if ppl_in_cars < ppl:
                return 'IMPOSSIBLE'
            cars[town] = i

    return ' '.join(map(str, cars[1:]))
    
T = int(inp())
for t in range(T):
    N, office = nl()
    E = ni()
    empl = [nl() for _ in range(E)]
    R = solve(N, office, empl)

    print('Case #{}: {}'.format(t+1, R))

