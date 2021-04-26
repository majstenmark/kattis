import sys
from collections import defaultdict as dd

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())


N, M, K = nl()
alp = {}
for i in range(26):
    a = chr(ord('A') + i)
    alp[a] = i + M + N

g = dd(list)

for i in range(N):
    line = inp()
    for c, ch in enumerate(line):
        ind = alp[ch]
        g[c].append(ind)
        g[ind].append(c)


def bfs(q, g):
    for node in q:
        visited.add(node)
    while q:
        q2 = []
        for node in q:
            for ne in g[node]:
                if ne not in visited:
                    visited.add(ne)
                    q2.append(ne)
        q = q2
    


visited = set()
color = 0
for i in g.keys():
    if i not in visited:
        color += 1
        bfs([i], g)
print(color)
        

