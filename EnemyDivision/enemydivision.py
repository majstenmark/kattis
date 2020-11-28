N , M = map(int, raw_input().split())
g = [[] for _ in range(N)]
WHITE = -1
BLACK = 1
def isUnhappy(node):
    same = 0
    diff = 0
    for ne in g[node]:
        if colors[ne] == colors[node]:
            same += 1
        else:
            diff += 1
    return same >= 2

colors = [WHITE for _ in range(N)]
for m in range(M):
    a, b = map(int, raw_input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
unhappy = set()
for node in range(N):
    if isUnhappy(node):
        unhappy.add(node)

if len(unhappy) == 0:
    print '1'
    s = ' '.join([str(x+1) for x in range(N)])
    print s
    exit()

while unhappy:
    for change in unhappy: break
    unhappy.remove(change)
    if isUnhappy(change):
        colors[change] = - colors[change]
        for ne in g[change]:
            if isUnhappy(ne):
                unhappy.add(ne)
            else:
                if ne in unhappy:
                    unhappy.remove(ne)

whites = []
blacks = []
for node in range(N):
    if colors[node] == WHITE:
        whites.append(str(node+1))
    else:
        blacks.append(str(node+1))
w = ' '.join(whites)
b = ' '.join(blacks)
print '2'
print w
print b
