import math
timetable = []
INF = 10**12

def dist(m1, m2):
    dX = mice[m1][0] - mice[m2][0]
    dY = mice[m1][1] - mice[m2][1]
    return math.sqrt(dX **2 + dY **2)

def latestStartTime(mouse, miceLeft, currentSpeed):
    if miceLeft == 0:
        return mice[mouse][2]
    #print(timetable)
    #print('mouse {} and miceleft {}'.format( mouse, bin(miceLeft)[2:]))
    if timetable[mouse][miceLeft] < INF:
        return timetable[mouse][miceLeft]
    latest = -1
    for bitIndex in range(N):
        if miceLeft & (1 << bitIndex):
            theRest = miceLeft ^ (1 << bitIndex)
            timetowalk = dist(mouse, bitIndex)/currentSpeed
            time = (latestStartTime(bitIndex, theRest, currentSpeed * M) -
            timetowalk)
            time = min(time, mice[bitIndex][2] - timetowalk)
            latest = max(latest, time)
    timetable[mouse][miceLeft] = latest
    return latest

def getStartTime(startSpeed):
    global timetable
    timetable = [[INF for subset in range(2 ** N)] for _ in range(N)]
    latest = -1
    allMice = 2 ** N - 1
    for bitIndex in range(N):
        theRest = allMice ^ (1 << bitIndex)
        timetowalk =  math.sqrt(mice[bitIndex][0] ** 2 + mice[bitIndex][1] ** 2)/startSpeed
        time = (latestStartTime(bitIndex, theRest, startSpeed * M) - timetowalk)
        time = min(time, mice[bitIndex][2] - timetowalk)
        latest = max(latest, time)
    return latest

N = int(raw_input())
mice = []
for n in range(N):
    x, y, s = map(int, raw_input().split())
    mice.append((x, y, s))
M = float(raw_input())
maxSpeed = 10**6 # all hide at 1 and are super far away from each other
minSpeed = 0.00000
count = 0
done = False
while not done:
    midSpeed = (minSpeed + maxSpeed)/2
    latest = getStartTime(midSpeed)
    #s = 'speed {} and latest start time {}'.format(midSpeed, latest)
    #print(s)
    if latest >=0:
        # ok
        maxSpeed = midSpeed
    else:
        minSpeed = midSpeed
    count += 1
    if count > 30:
        done = True
print(minSpeed)
