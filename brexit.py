C,P,X,L = map(int,raw_input().split())
g = [[] for _ in range(C)]
for p in range(P):
    a,b=map(int,raw_input().split())
    g[a -1].append(b -1)
    g[b-1].append(a-1)
q = []
q.append(L-1)
lives = [(len(g[n]) +1)/2 for n in range(C)]
lives[L-1] = 0

while q:
    q2 = []
    for c in q:
        for p in g[c]:
            if lives[p] >= 1:
                lives[p] -= 1
                if lives[p] <= 0:
                    q2.append(p)

    q = q2
if lives[X-1]>0:
    print('stay')
else:
    print('leave')
