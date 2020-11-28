import heapq
inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

n = ni()
st = nl()

L=[set() for _ in range(n)]
R = [set() for _ in range(n)]
for i in range(n):
    x = st[i] 
    s = i + x
    if s < n:
        L[s].add(i)
    s = i -x
    if s >= 0:
        R[s].add(i)

q = [0]
visited = set(q)
while q:
    q2 = []
    for u in q:
        r = u + st[u]
        l = u - st[u]
        if r < n:
            for v in R[r]:
                if v not in visited:
                    visited.add(v)
                    q2.append(v)
        if l >= 0:
            for v in L[l]:
                if v not in visited:
                    visited.add(v)
                    q2.append(v)
    q = q2
print(max(visited))
