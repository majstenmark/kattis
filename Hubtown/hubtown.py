import math

def getOnePath(path):
        s = 0

        pairs = []
        while path[s] > -1:
            pairs.append((s, path[s]))
            s = path[s]
        return pairs

def solveCycle(rays,capacity, passangers, assignments, path):
    #startnode in rail 0
    s = 0
    pairs = getOnePath(path)
    lo = 0
    hi = min(capacity[s], len(passangers[pairs[0]]))

    for a, b in pairs:
        minLeft = len(passangers[(a, b)] - hi # the ones that were not in the previous train
        maxLeft = len(passangers[(a, b)] - lo
        lo = min(capacity[b], minLeft)
        hi = min(capacity[b], maxLeft)
        if hi <= lo:
            
    # and what happened in the en?
    return


def getPath(path):
    all = [True for _ in range(M)]
    for n in range(M):
        if path[n] > -1:
            all[path[n]] = False
    s = 0
    for n in range(M):
        if all[n]:
            s = n
            break

    pairs = []
    while path[s] > -1:
        pairs.append((s, path[s]))
        s = path[s]
    return pairs


def solvePaths(rays,capacity, passangers, assignments, path):
    pairs = getPath(path)

    print('pairs {}'.format(pairs))


    for a, b in pairs:
        print('a, b: ', a, b)
        ppl = min(len(passangers[(a, b)]), capacity[a])
        print('ppl ', ppl)
        for index in range(ppl):
            passanger = passangers[(a, b)][index]
            assignments[passanger] = a # ID!
            capacity[a] -= 1
        # fill the next train!

        ppl2 = min(len(passangers[(a, b)]) - ppl, capacity[b])
        print('ppl2 ', ppl2)
        for index in range(ppl2):
            passanger = passangers[(a, b)][index + ppl]
            assignments[passanger] = b
            print('Passenger {} gets train {}'.format(passenger, b))
            capacity[b]-= 1


N, M = map(int, raw_input().split())
commuters = []
rays = []
capacity = []
path = [-1 for _ in range(M)]

for n in range(N):
    x, y = map(int, raw_input().split())
    angle = math.atan2(x, y)
    commuters.append((angle, n))
for m in range(M):
    x, y, c = map(int, raw_input().split())
    angle = math.atan2(x, y)
    rays.append([angle, m])
    capacity.append(c)
    deg = angle / math.pi * 180
    print('Ray angle {} id {}'.format(deg, m))
commuters.sort()
rays.sort()
# build a graph
minAngle = rays[-1][0] -2 * math.pi
maxRayIndex = 0
tmp = {}

for n in range(N):
    angle, id = commuters[n]

    deg = angle / math.pi * 180
    print('Person angle {} id {} ({})'.format(deg, (id + M), id))
    dd= rays[maxRayIndex][0] /math.pi * 180
    ddd= minAngle /math.pi * 180
    while angle > rays[maxRayIndex][0] and maxRayIndex < M:
        minAngle = rays[maxRayIndex][0]
        maxRayIndex += 1

    print('Angle above {} and minangle {}'.format(dd, ddd))
    print('D1 {} and D2 {}'.format(abs(angle - rays[maxRayIndex][0]), abs(angle - minAngle)))

    if abs(abs(angle - rays[maxRayIndex][0]) - abs(angle - minAngle)) < 10 ** -6:
        # same distance
        print('Person {} same dist to {} and {}'.format((id+M), minAngle, rays[maxRayIndex][0]))
        aId = rays[maxRayIndex][1]
        bId = rays[((maxRayIndex - 1) % M)][1]
        aId, bId = min(aId, bId), max(aId, bId)
        if not (aId, bId) in tmp:
            tmp[(aId, bId)]= []
            path[aId] = bId
        tmp[(aId, bId)].append(id)

    elif abs(angle - rays[maxRayIndex][0]) < abs(angle - minAngle):
        aId = rays[maxRayIndex][1]
        print('Person {} closest to {}'.format((id+M), aId))
        if not aId in tmp:
            tmp[(aId, -1)]= []
        tmp[(aId, -1)].append(id)
    else:
        aId = rays[((maxRayIndex - 1) % M)][1]

        print('Person {} closest to {}'.format((id+M), aId))
        if not aId in tmp:
            tmp[(aId, -1)]= []
        tmp[(aId, -1)].append(id)

edges = 0
assignments = [-1 for _ in range(N)]
print(tmp)
print('rays b4 assignments ', rays)
for a, b in tmp:
    if b >= 0:
        edges += 1
    else:
        # assign to train!
        ass = min(len(tmp[(a, b)]), capacity[a])
        for k in range(ass):
            passenger = tmp[(a, b)][k]
            print('Single assignment {} to {}'.format((passenger + M), a))
            assignments[passenger] = a
            capacity[a] -= 1
# testa
# if cycle
print('rays ', rays)
if edges ==  M:
    #solveCycle(g)
    # cycle
    print('Cycle!')
else:
    # paths!

    print('Paths!')
    solvePaths(rays, capacity, tmp, assignments, path)
    print(assignments)
    #for index in range(N):
    #    if assignments[index] > -1:
    #        print('{} {}'.format(index, assignments[index]))
