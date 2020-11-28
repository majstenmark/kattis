INF = 10**12
T = int(raw_input())
for t in range(T):
    M = int(raw_input())
    dists = map(int, raw_input().split())
    hs = [[[INF, -1] for _ in range(1002)] for m in range(M+1)]
    hs[0][0] = [0, 0]

    for index, dist in enumerate(dists):
        for h in range(1001):
            maxH, dir = hs[index][h]

            if dir != -1:
                up = h + dist
                prevMax, prevDir = hs[index +1][up]

                if max(maxH, up) < prevMax:

                    hs[index+1][up] = [max(maxH, up), 1]
                    #print 'updating hs {} {} with {} {} coming from {}'.format(index+1, up, max(maxH, up), 1, h)
                down = h - dist
                if down >= 0:
                    prevMax, prevDir = hs[index + 1][down]
                    if maxH < prevMax:

                #        print 'downdating '
                    #    print 'updating hs {} {} with {} {} coming from {}'.format(index+1, down, maxH, 0, h)
                        hs[index+1][down] = [maxH, 0]


    if hs[-1][0][1] == -1:
        print 'IMPOSSIBLE'
    else:
        d = len(dists)
        path = []
        currH = 0
        while d > 0:
            maxH, dir = hs[d][currH]
            path.append('U' if dir == 1 else 'D')
            if dir == 1:
                oldH = currH
                currH = currH - dists[d-1]

            #    print 'd {} to {} from {} dr {}'.format(d, oldH, currH, dir)
            else:
                oldH = currH
                currH = currH + dists[d-1]

            #    print 'd {} to {} from {} dr {}'.format(d, oldH, currH, dir)
            d -= 1
        res = ''.join(path[::-1])
        print res
