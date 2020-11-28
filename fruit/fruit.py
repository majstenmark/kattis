def smallCombos(pieces):
    totW = 0
    n = len(pieces)
    for i in range(n):
        w = pieces[i]
        totW += w
        #print('added ', w)
        for j in range(i + 1, n):
            wstartJ = w
            w += pieces[j]
            if w < 200:
                totW += w
                #print('added ', w)
                for k in range(j +1, n):
                    wstartK = w
                    w += pieces[k]
                    if w < 200:
                        totW += w
                        #print('added ', w)
                    w = wstartK
            w = wstartJ
    return totW

N = int(raw_input())
ws = [int(v) for v in raw_input().split()]
smallPieces = filter(lambda x:x < 200, ws)
baskets = 2 ** (N-1)
totWeight = baskets *sum(ws)
smallWeights = smallCombos(smallPieces)
#print(totWeight)
#print(smallWeights)
print(totWeight - smallWeights)
