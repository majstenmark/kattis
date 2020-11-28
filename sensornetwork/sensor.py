from collections import deque

sensors = []
parents = []
def find(x):
    if parents[x][0] != x:
        parents[x][0] = find(parents[x][0])
    return parents[x][0]

def add(a, a_parent, b_parent):

    p,size= parents[b_parent]
    size += parents[a_parent][1]
    parents[b_parent] =  [b_parent, size]
    parents[a_parent][0] = b_parent

def union(a,b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent == b_parent:
        return False

    if parents[a_parent][1] < parents[b_parent][1]:
        add(a,a_parent, b_parent)
    else:
        add(b, b_parent,a_parent)
    return True

def buildTreeDownwards(sensorsInTree):

    newSensorsInTree = deque()

    for x in range(N):
        parents[x] = [x,1]
    counter = 0
    for w, a,b in sensorsInTree:
        success = union(a, b)
        if success:
            newSensorsInTree.append((w, a,b))
            counter += 1

    connected = counter == N - 1
    altMargin = abs(newSensorsInTree[len(newSensorsInTree)-1][0] - newSensorsInTree[0][0])
    return (connected,  altMargin, newSensorsInTree)


N = int(raw_input())
while N != 0:
    sensors = []
    M = int(raw_input())
    for m in range(M):
        a, b, w = map(int, raw_input().split())
        sensors.append((w, a, b))
    parents = [[x, 1] for x in range(N)]

    sensors.sort()
    sensorsInTree = deque()
    nextSensorIndex = 0
    margin = abs(sensors[-1][0] - sensors[0][0])
    while nextSensorIndex < M:
        sensorsInTree.appendleft(sensors[nextSensorIndex])
        while len(sensorsInTree) > 1 and sensorsInTree[0][0] - sensorsInTree[len(sensorsInTree)-1][0] >= margin:
            sensorsInTree.pop()
        if len(sensorsInTree) >= N-1:
            connected,  altMargin, sensorsInTree = buildTreeDownwards(sensorsInTree)
            if connected:
                margin = min(margin, altMargin)
        nextSensorIndex += 1

    print(margin)
    raw_input()
    N = int(raw_input())
