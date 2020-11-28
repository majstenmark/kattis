def setAllConnected(colored, g, lounges):
    newlyUpdated = []
    newlyUpdated.extend(colored)
    while colored:
        colored2 = []
        for node in colored:
            for ne, c in g[node]:
                if c == 1:
                    if lounges[ne] == UNDEC:
                        lounges[ne] = -lounges[node]
                        newlyUpdated.append(ne)
                        colored2.append(ne)
                    elif lounges[ne] != -lounges[node]:
                        failed()
        colored= colored2
    return newlyUpdated

def failed():
    print('impossible')
    exit(0)
N, M = map(int, raw_input().split())
twoC = []
zeroC = []
oneC = []
g = [[] for _ in range(N)]
for m in range(M):
    a, b, c = map(int, raw_input().split())
    a -= 1
    b -= 1
    if c == 0:
        zeroC.append((a, b))
    elif c == 1:
        oneC.append((a, b))
    else:
        twoC.append((a, b))
    g[a].append((b, c))
    g[b].append((a, c))
UNDEC = 0
WITH = 1
WOUT = -1
RED = 2
BLUE = -2
colored = []
lounges = [UNDEC for _ in range(N)]
for a, b in twoC:
    if lounges[a] == UNDEC:
        lounges[a] = WITH
        colored.append(a)

    if lounges[b] == UNDEC:

        lounges[b] = WITH
        colored.append(b)
for a, b in zeroC:
    if lounges[a] == WITH or lounges[b] == WITH:
        failed()

    lounges[a] = WOUT
    colored.append(a)
    lounges[b] = WOUT
    colored.append(b)

setAllConnected(colored, g, lounges)
setLounges = 0
for node in range(N):
    if lounges[node] == WITH:
        setLounges += 1
minReds = 0
for a, b, in oneC:
    if lounges[a] == UNDEC and lounges[b] == UNDEC:
        lounges[a] = RED
        colored = [a]
        updated = setAllConnected(colored, g, lounges)
        reds = 0
        blues = 0
        for node in updated:
            if lounges[node] == RED:
                reds += 1
            else:
                blues += 1
        minReds += min(reds, blues)

tot = setLounges + minReds
print tot

# some are still both zero!
