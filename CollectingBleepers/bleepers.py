N = input()

def manh(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def helper():
    visited = 2 ** B -1
    if B == 0:
        return 0
    alt = INF
    for other in range(B):
        mask = visited ^ 1 << other
        alt = min(alt, manh(start, bleeps[other]) + mindist(other, mask))
    #    print 'from start', start, other, 'pos', bleeps[other], 'dist ', manh(start, bleeps[other])
    return alt

def mindist(bleeper, visited):
    if cost[bleeper][visited] < INF:
        return cost[bleeper][visited]
    alt = INF
    for other in range(B):
        if 1 << other & visited:
            mask = visited ^ 1 << other
            alt = min(alt, manh(bleeps[bleeper], bleeps[other]) + mindist(other, mask))
    cost[bleeper][visited] = alt
    return cost[bleeper][visited]

for t in range(N):
    x, y = map(int, raw_input().split())

    sx, sy = map(int, raw_input().split())
    start = [sx, sy]
    B =input()
    bleeps = []
    for b in range(B):
         bleeps.append(map(int, raw_input().split()))
    INF = 10**12
    cost = [[INF for b in range(2 ** B)] for _ in range(B)]
    #print bleeps
    for index, pos in enumerate(bleeps):
        d= manh(pos, start)
        cost[index][0] =  d # only the last node
    print helper()
