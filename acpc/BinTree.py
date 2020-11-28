MOD = 21092013
N = int(raw_input())
for n in range(N):
    S = raw_input()
    T = raw_input()
    stack = []
    for ch in S:
        if ch == 'R' or ch == 'L':
            stack.append(ch)

        elif len(stack)> 0:
            stack.pop()
    depth = len(stack)

    cnt = [0] * (len(T) + 2)
    cnt[-2] = 1
    #cnt[-3] = 2

    L = [len(cnt) -1] * (len(cnt))
    R = [len(cnt) -1] * (len(cnt))

    #print cnt
    for i in range(len(T) - 1, -1, -1):
        last = T[i]
        R[i] = R[i+1]
        L[i] = L[i+1]

        if last == 'L':
            cnt[i] = (1 + cnt[i+1] + cnt[R[i]]) % MOD

        #    print 'index', i,cnt, lastL, lastR
            L[i] = i + 1

        elif last == 'R':
            cnt[i] = (1 + cnt[i + 1] + cnt[L[i]]) % MOD
            R[i] = i + 1
        #    print 'index', i,cnt, lastL, lastR
        else:
            cnt[i] = cnt[i + 1]

    totCnt = cnt[0]
    for index, ch in enumerate(T):
        if ch == 'U':
            if len(stack) == 0:
                break
            dir = stack.pop()
            if dir == 'L':
                nextIndex = R[index]
            else:
                nextIndex = L[index]
        #    print 'nextIndex', nextIndex,  cnt[nextIndex + 1]
            totCnt = (totCnt + 1 + cnt[nextIndex]) % MOD

    print 'Case {}: {}'.format(n+1, totCnt)
