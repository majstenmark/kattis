T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    nameToPosInDl = [0 for _ in range(N+1)]
    dlToPosInSL = [x for x in range(N+1)]
    topDl = set()
    for index in range(1,N + 1):
        dlRank = int(raw_input())
        nameToPosInDl[index] = dlRank
        dlToPosInSL[dlRank] = index
    personInSl = 1
#    print('nameToPosInDl: {}'.format(nameToPosInDl))
#    print('dlToPosInSL: {}'.format(dlToPosInSL))
    phys  = []
    for personInDl in range(1, N+1):
        posInSL = dlToPosInSL[personInDl] # which is also the name
        topDl.add(posInSL)
        while personInSl <= posInSL:
            if personInSl not in topDl:
                phys.append(nameToPosInDl[personInSl]) #their position in DL
            personInSl += 1
    s = '\n'.join(map(str, sorted(phys)))
    print(str(len(phys)))
    if s: print(s)
