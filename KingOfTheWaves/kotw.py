N = int(raw_input())
g = [[] for _ in range(N)]
for n in range(N):
    line = raw_input()
    for index in range(len(line)):
        if line[index] == '1':
            g[n].append(index)
layers = []
visited = [False] * N
q = [0]

layers.append(q)
for node in q:
    visited[node] = True
while q:
    q2 = []
    for node in q:
        for ne in g[node]:
            if not visited[ne]:
                visited[ne] = True
                q2.append(ne)
    q = q2
    layers.append(q)

def checkAll():
    for node in range(N):
        if not visited[node]:
            return False
    return True
if not checkAll():
    print('impossible')
else:
    seq = []
    for layer in layers[::-1]:
        for player in layer:
            seq.append(str(player))
    s = ' '.join(seq)
    print(s)
