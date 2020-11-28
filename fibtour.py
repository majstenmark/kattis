from heapq import heappop as pop, heappush as push
from collections import defaultdict as dd
# dep, is parent count, g = parents
def topsort(nodes, dep,g):
    li = []
    q = []
    for node in nodes:
        push(q, (dep[node], node))
    while q:
        p, f = pop(q)
        if p == 0:
            li.append(f)
            for d in g[f]:
                dep[d] -= 1
                push(q, (dep[d], d))
    return li

def depth(li, g):
    cnt = dd(lambda:1)
    for node in li[::-1]:
        for ch in g[node]:
            cnt[node] = max(cnt[ch] + 1, cnt[node])
    return cnt 

N, M = [int(v) for v in raw_input().split()]
H = [int(v) for v in raw_input().split()]
forward = {}

f1, f2 = 1, 1

for i in range(2, 80):
    next = f1 + f2
    forward[f2] = next

    if next > 10**18:
        break
    f1, f2 = f2, next

g = [[] for _ in range(N)]

dep = [0] * N

to2 = set()
to1 = set()

nodes = set()
for m in range(M):
    a, b = [int(v) -1 for v in raw_input().split()]
    if H[a] in forward:
        nodes.add(a) 
    if H[b] in forward:
        nodes.add(b)
    
    if H[a] in forward and H[b] in forward:
        
        if forward[H[a]] == H[b]:
            g[a].append(b)
            dep[b] += 1
        if forward[H[b]] == H[a]:
            g[b].append(a)
            dep[a] += 1
        
        if H[a] == 1:  
            if H[b] == 2:
                to2.add(a)
            if H[b] == 1:
                to1.add(a)

        if H[b] == 1:  
            if H[a] == 2:
                to2.add(b)
            if H[a] == 1:
                to1.add(b)


firsts = []

li = topsort(nodes, dep, g)
cnt = depth(li, g)
print('li', li)
best = 0 if len(nodes) == 0 else 1
print(cnt)

for node in nodes:
    alt = cnt[node]
    if node in to1 and node in to2:
        alt += 1
    best = max(best, alt)

print(best)



