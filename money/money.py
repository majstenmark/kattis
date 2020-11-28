def find(x):
    if parents[x][0] != x:
        parents[x][0] = find(parents[x][0])
    return parents[x][0]

def add(a, a_parent, b_parent):

    p,size,ssum= parents[b_parent]
    size += parents[a_parent][1]
    ssum += parents[a_parent][2]
    parents[b_parent] =  [b_parent, size, ssum]
    parents[a_parent][0] = b_parent

def union(a,b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent == b_parent:
        return

    if parents[a_parent][1] < parents[b_parent][1]:
        add(a,a_parent, b_parent)
    else:
        add(b, b_parent,a_parent)

N, M = map(int, raw_input().split())
parents = []

for n in range(N):
    balance = int(raw_input())
    parents.append([n, 1, balance])

for m in range(M):
    personA, personB = map(int, raw_input().split())
    union(personA, personB)

for person in range(N):
    if parents[person][0] == person:
        if parents[person][2] != 0:
            print('IMPOSSIBLE')
            exit(0)
print('POSSIBLE')
