import math
def isprime(n):
    if n == 1: return False

    v =int(math.ceil(math.sqrt(n)))
    for i in range(2, min(v + 1, n)):
        if n % i == 0:
            return False
    return True
def getHighestPrime(n):
    for nbr in range(n, -1, -1):
        if isprime(nbr):
            return nbr
    return 0

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

T = int(raw_input())
for i in range(T):
    N, D = map(int, raw_input().split())
    flowerCoords = []
    for n in range(N):
        x, y = map(int, raw_input().split())
        flowerCoords.append((x, y))

    walkedDist = 0
    cont = True
    nextFlower = 0
    currentPos = (0, 0)
    while cont and nextFlower < N:
        distToNext = dist(flowerCoords[nextFlower], currentPos)
        if walkedDist + distToNext > D:
            cont = False
        else:
            walkedDist += distToNext
            currentPos = flowerCoords[nextFlower]
            nextFlower += 1
    res = getHighestPrime(nextFlower)
    print(res)
