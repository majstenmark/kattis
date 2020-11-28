import sys
INF = 10**12

def binarySearch(endingNbr, k, v):
    minK = 0
    maxK = k
    while minK < maxK:
        midK = (maxK + minK)/2

        if endingNbr[midK][0] < v:
            minK = midK + 1
        elif endingNbr[midK][0] > v:
            maxK = midK
        else:
            return False, midK
    return True, maxK

def findLis(N, seq):
    endingNbr = [(INF, -1) for _ in range(N)]
    index = [-1] *N
    maxI = 0
    endingNbr[0] = (seq[0], 0)
    for k in range(1, N):
        v = seq[k]
        update, toK = binarySearch(endingNbr, maxI + 1, v)
    #    print 'got value', update, toK
        if update:
            endingNbr[toK] = min(endingNbr[toK], (v, k))
            index[k] = endingNbr[toK -1][1]
            maxI = max(maxI, toK)
        #    print 'ending ', endingNbr
    li = []
    i = endingNbr[maxI][1]
    while i != -1:
        li.append(i)
        i = index[i]

    return li[::-1]



indata = sys.stdin.readlines()
for test in range(0, len(indata), 2):
    N = int(indata[test])
    seq = map(int, indata[test+1].split())
    li = findLis(N, seq)
    print len(li)
    print ' '.join(map(str, li))
