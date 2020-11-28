import bisect

try:

    def finds(q, i):
        index = bisect.bisect(i, q)
    #    print 'index to {} is {}'.format(q, index)
    #    print i
        if index == 0:
            return i[0] + i[1]
        hi = min(index + 1, len(i)-1)
        lo = 0
        cand = i[hi] + i[lo]
        if cand == q or hi == lo + 1:
            return cand
    #    print 'start cand to {}: {}'.format(q, cand)
        best = cand
        while True:
            if cand < q:
                lo += 1
            if cand > q:
                hi -= 1

            cand = i[hi] + i[lo]

            best = cand if abs(cand - q) < abs(best - q) else best
        #    print 'q {} new cand {} best {}, lo {} hi {}'.format(q,cand, best, lo, hi)

            if best == q:
                return best
            if hi == lo + 1:
                return best



    case = 1
    while True:
        N = input()
        i = []
        for n in range(N):
            i.append(input())
        i.sort()
        M = input()
        print 'Case {}:'.format(case)
        for _ in range(M):
            q = input()
            s = finds(q, i)
            print 'Closest sum to {} is {}.'.format(q, s)
        case += 1
except:
    exit()
