N, M = map(int, raw_input().split())
edges= []
for p in range(M):
    a, b = map(int, raw_input().split())
    edges.append((a - 1,b-1))
parents = [(n, 1) for n in range(N )]
def find(x):
    if parents[x][0] != x:
        parents[x] = find(parents[x][0])
    return parents[x]

def union(setA, setB):
    if setA[1] > setB[1]:
        parents[setA[0]] = (setA[0],setB[1] + setA[1] )
        parents[setB[0]] = setA
    else:
        parents[setB[0]] = (setB[0],setB[1] + setA[1] )
        parents[setA[0]] = setB


for (a,b) in edges:
    setA = find(a)
    setB = find(b)
#    s = 'edge {}--{}, setA {} and setB {}'.format(a,b,setA, setB)
#    print(s)
    if setA[0] != setB[0]:
        union(setA, setB)
        setA = find(a)
        setB = find(b)
#        s = 'After union edge {}--{}, setA {} and setB {}'.format(a,b,setA, setB)
#        print(s)
internet = find(0)
if internet[1] == N:
    print('Connected')
else:
    for nn in range(N):
        if find(nn)[0] != internet[0]:
            index = nn+1
            print(index)
