n, k, t1, t2 = map(int, raw_input().split())
ms = []
END = 1
START = 0
measurements = raw_input().split()
for measurement in measurements:
    m = int(measurement)
    ms.append(m)

suns = []
for deadzone in range(k):
    b, e = map(int,raw_input().split())
    suns.append((b, e))

def deadinterval(fb, fe, m):
     start = max(t1, fb - m)
     end = min(t2, fe - m)
     return (start, end)

forbiddenIntervals = []
for m in ms:
    for fb, fe in suns:
        start, end = deadinterval(fb, fe, m)
        forbiddenIntervals.append((start, START))
        forbiddenIntervals.append((end, END))
        

forbiddenIntervals.sort()
deadTime = 0
totDeadTime = 0.0
counter = 0
for event, eventType in forbiddenIntervals:
    if eventType == START:
        if counter == 0:
            deadTime = event
        counter += 1
    else:
        counter -= 1
        if counter == 0:
            totDeadTime += (event - deadTime)
totalTime = t2 - t1
prob = (totalTime - totDeadTime)/totalTime
print(prob)
