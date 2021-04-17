import sys
from heapq import heappush as push, heappop as pop

def setdist(child):
    dist = [0] * N
    q = [0]
    while q:
        q2 = []
        for node in q:
            for c in child[node]:
                dist[c] = dist[node] + 1
                q2.append(c)
        
        q = q2
    return dist

def check(d, i):
    cnt = 1
    p = parent[i]
    for i in range(d):
        if used[p]:
            return cnt
        p = parent[p]
        cnt += 1
    return cnt

def use(i):
    used[i] = True
    p = parent[i]
    while not used[p]:
        used[p] = True
        p = parent[p]

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N, K = nl()
skills = nl()

parent = [None] + [ni() for _ in range(N-1)]

child = [[] for _ in range(N)]

for c, p in enumerate(parent[1:]):
    child[p].append(c+1)

dist = setdist(child)
used = [False] * N
used[0] = True
skills.sort()
l = []
for i, d in enumerate(dist):
    push(l, (-d, i))
su = 0
#print(dist)
fin = 0
while fin < K:
    minus_d, i = pop(l)
    new_d = check(-minus_d, i)
    #print(f'Checking len for {i} res = {new_d}')
    if -minus_d == new_d:
        s = skills.pop()
        su += s * new_d
        use(i)
        fin += 1
        #print(f'Curr su = {su}')
    else:
        push(l, (-new_d, i))
print(su)