R, C  = map(int, raw_input().split())
f = [['.' for _ in range(C)] for x in range(R)]
INF = 10**12
time = [[INF for _ in range(C)] for x in range(R)]

hh = (0, 0)
den = (0, 0)
floods = []
for r in range(R):
    row = raw_input()
    for c in range(C):
        ch = row[c]
        if ch == 'D':
            den = (r, c)
            f[r][c] = ch
        elif ch == 'S':
            hh = (r,c)
        elif ch == '*':
            floods.append((r,c))
            f[r][c] = ch
        else:
            f[r][c] = ch

def nei(node):
    ne = []
    x = node[0]
    y = node[1]
    cand = [(x +1, y), (x -1, y), (x, y+1), (x, y-1)]
    for cx, cy in cand:
        if 0 <= cx < R and 0 <= cy < C and f[cx][cy] == '.':
            ne.append((cx,cy))
    return ne

def bfs(q):
    visited = set()
    for node in q:
        visited.add(node)

        time[node[0]][node[1]] = 0
    mins = 1
    while q:
        q2 = []
        for node in q:
            for ne in nei(node):
                if ne not in visited:
                    visited.add(ne)
                    time[ne[0]][ne[1]] = mins
                    q2.append(ne)
        q = q2
        mins += 1

def neiS(node,t):
    ne = []
    x = node[0]
    y = node[1]
    cand = [(x +1, y), (x -1, y), (x, y+1), (x, y-1)]
    for cx, cy in cand:
        if 0 <= cx < R and 0 <= cy < C and (f[cx][cy] == '.' or f[cx][cy] == 'D') and time[cx][cy] > t:
            ne.append((cx,cy))
    return ne

def bfsS():
    visited = set()

    visited.add(hh)
    mins = 0
    q = [hh]
    while q:
        q2 = []
        for node in q:
            if node == den:
                return mins
            for ne in neiS(node, mins +1):
                if ne not in visited:
                    visited.add(ne)
                    q2.append(ne)
        q = q2
        mins += 1
    return -1

bfs(floods)

p = bfsS()
if p == -1:
    print 'KAKTUS'
else:
    print p
