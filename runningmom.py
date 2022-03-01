import sys
from collections import defaultdict as dd
sys.setrecursionlimit(100000)

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
g = dd(list)
for _ in range(N):
    a, b, = inp().split()
    g[a].append(b)

def dfs(node, visited):
    if node in visited:
        return True
    visited.add(node)
    for ne in g[node]:
        if dfs(ne, visited):
            return True
        visited.discard(ne)
    return False

out = []

while True:
    city = inp()
    if city == "": break
    if dfs(city, set()):
        print(f'{city} safe')
    else:
        print(f'{city} trapped')
    
print('\n'.join(out))




