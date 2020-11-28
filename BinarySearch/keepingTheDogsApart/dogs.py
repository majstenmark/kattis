import math

N = int(raw_input())
shadow = []
for n in range(N):
    x, y = map(int, raw_input().split())
    shadow.append((x, y))
M = int(raw_input())
lydia = []
for m in range(M):
    x, y = map(int, raw_input().split())
    lydia.append((x, y))
i = 0
k = 0
INF = 10 ** 12

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def projection(p1, p2):
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    c = -a*p1[0] - b * p1[1]
    ab2 = a **2 + b ** 2
    if abs(ab2) < 10 ** -8:
        return INF
    x = -a * c / ab2
    y = - b * c /ab2
    minX = min(p1[0], p2[0]) - 10 ** -8
    maxX = max(p1[0], p2[0]) +  10 ** -8
    minY = min(p1[1], p2[1]) - 10 ** -8
    maxY = max(p1[1], p2[1]) +  10 ** -8
    if minX < x < maxX and minY < y < maxY:
        return abs(c)/math.sqrt(ab2)
    else:
        return min(dist(p1, (0, 0)), dist(p2, (0, 0)))


# fix lydias position
walk = [(shadow[0][0] - lydia[0][0], shadow[0][1] - lydia[0][1])]

while k < M - 1 and i < N - 1:
    distA = dist(shadow[i + 1], shadow[i])
    distB = dist(lydia[k+1], lydia[k])
    distC = min(distA, distB)
    sX = shadow[i][0] + distC/distA * (shadow[i +1][0] - shadow[i][0])
    sY = shadow[i][1] + distC/distA * (shadow[i +1][1] - shadow[i][1])

    lX = lydia[k][0] + distC/distB * (lydia[k +1][0] - lydia[k][0])
    lY = lydia[k][1] + distC/distB * (lydia[k +1][1] - lydia[k][1])
    x = sX - lX
    y = sY - lY

    #print('{} {} {} {} {} {}'.format(distA,distB, sX, sY, lX, lY))
    lydia[k] = (lX, lY)

    shadow[i] = (sX, sY)
    if dist(lydia[k+1], lydia[k]) < 10 ** (-8):
        k += 1
    if dist(shadow[i+1], shadow[i]) < 10 ** (-8):
        i += 1
    walk.append((x,y))
minDist = dist(walk[-1], (0,0))
#walk.append((shadow[i][0] - lydia[k][0], shadow[i][1] - lydia[k][1]))
dists = []
for segment in range(len(walk) -1):
    dists.append(projection(walk[segment], walk[segment + 1]))
    minDist = min(minDist, projection(walk[segment], walk[segment + 1]))
print(minDist)
