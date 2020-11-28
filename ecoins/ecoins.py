import math
N = int(raw_input())
for n in range(N):
    M, S = map(int, raw_input().split())
    coins = []
    for m in range(M):
        c, i = map(int, raw_input().split())
        coins.append((c, i))
    INF = 10**12
    dist = [[INF]*(S + 1) for _ in range(S + 1)]
    dist[0][0] = 0
    S2 = S **2
#    print(coins)
    for x in range(S):
        for y in range(S):
            for c, i in coins:
                if x + c <= S and y + i <= S:
                    dist[x + c][y + i] = min(dist[x][y] + 1, dist[x + c][y + i])
    count = INF
#    print(dist)
    for x in range(S + 1):
        x2= x **2
        y2 = S2 - x2
        y = int(round(math.sqrt(y2), 0))
        if y**2 + x2 == S2:
            count = min(count, dist[x][y])

    if count == INF:
        print('not possible')
    else:
        print(count)
    try:
        raw_input()
    except:
        exit()
