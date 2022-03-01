import sys
from collections import defaultdict as dd
itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

parents = {}
size = dd(lambda: 1)

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def add(a_parent, b_parent):

    size[b_parent] += size[a_parent]
    parents[b_parent] = b_parent
    parents[a_parent] = b_parent

def union(a,b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent == b_parent:
        return size[a_parent]

    if size[a_parent] < size[b_parent]:
        add(a_parent, b_parent)
        return size[b_parent]
    else:
        add(b_parent,a_parent)
        return size[a_parent]
    return -1

N = ni()

def init(a):
    global id
    if a not in seen:
        ida = len(seen)
        seen[a]  = ida
    return seen[a]

out = []
seen = {}

bridges = []
for _ in range(N):
    a, b = inp().split()
    ida = init(a)
    idb = init(b)
    bridges.append((ida, idb))

N = len(seen)
parents = [i for i in range(N)]
size = [1] * N

for a, b in bridges:
    val = union(a, b)
    out.append(str(val))
print('\n'.join(out))

