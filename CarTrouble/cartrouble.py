from collections import defaultdict as dd

def bfs(node, g):
    visited = set()
    q  = [node]
    visited.add(node)
    while q:
        q2 = []
        for node in q:
            for ne in g[node]:
                if ne not in visited:
                    visited.add(ne)
                    q2.append(ne)
        q = q2
    return visited

N = input()
streets = {}
backstreets = dd(list)
for n in range(N):
    line = raw_input().split()
    id = int(line[0])
    turns = map(int, line[2:])
    streets[id] = []
    for t in turns:
        streets[id].append(t)
        backstreets[t].append(id)

S = set(streets.keys())

forward = bfs(0,streets)
backward = bfs(0, backstreets)
ok = True
for id in S.difference(backward):
    ok= False
    print 'TRAPPED {}'.format(id)

for id in S.difference(forward):
    ok = False
    print 'UNREACHABLE {}'.format(id)


if ok:
    print 'NO PROBLEMS'
