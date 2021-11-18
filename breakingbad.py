import sys
from collections import defaultdict as dd, Counter
itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def twocolor(g, color, start):
    if color[start] != 0:
        return True
    color[start] = 1
    q = [start]
    while q:
        q2 = []
        for node in q:
            for ne in g[node]:
                if color[ne] != 0:
                    if color[ne] == color[node]:
                        return False
                else:
                    color[ne] = - color[node]
                    q2.append(ne)
        q =q2
    return True


N = ni()
names = [inp() for _ in range(N)]
M = ni()
edges = [inp().split() for _ in range(M)]
g = dd(list)
for a, b in edges:
    g[a].append(b)
    g[b].append(a)

color = Counter()
ok = True

for name in names:
    ok = twocolor(g, color, name)
    if not ok: break

if ok:
    out = [[], []]
    for name, col in color.items():
        if col == 1:
            out[0].append(name)
        else:
            out[1].append(name)
    print(' '.join(out[0]))
    print(' '.join(out[1]))
else:
    print('impossible')
    

