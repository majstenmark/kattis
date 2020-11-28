T, N = map(int, raw_input().split())
W = []
E = []
WE = 1
EW = -1
for n in range(N):
    dir, a, r = raw_input().split()
    arr = int(a)
    irr = int(r)
    if dir == 'W':
        W.append((arr, arr+ irr))
    else:
        E.append((arr, arr + irr))

states = [{} for _ in range(N+1)]
states[0] = {(0, WE, 0): 0, (0, EW, 0): 0}
for n in range(1, N+1):
    for state in states[n - 1]:
        irritated, direction, westN = state
        endtime = states[n-1][state]
        eastN = n -1 - westN
    #    print 'state', state
    #    print 'est n', eastN
        nextArrival, nextDeadline = 0, 0
        if direction == WE and westN < len(W):
            nextArrival, nextDeadline = W[westN]
            westN += 1
        elif direction == EW and eastN < len(E):
            nextArrival, nextDeadline = E[eastN]
        else:
            continue
        nextStart = max(endtime, nextArrival)
        if nextStart > nextDeadline:
            irritated += 1
        sameEnd = nextStart + 3
        otherEnd = nextStart + T
        sameDirState = (irritated,direction,westN)
        otherDirState = (irritated, -direction,westN)
    #    print 'same dir state ', sameDirState
    #    print 'other dir state', otherDirState
        if sameDirState in states[n]:
            sameEnd = min(sameEnd, states[n][sameDirState])
        states[n][sameDirState] = sameEnd
        if otherDirState in states[n]:
            otherEnd = min(otherEnd, states[n][otherDirState])
        states[n][otherDirState] = otherEnd
minIrr = 1000
#print states
for state in states[-1]:
        irritated, direction, westN = state
        minIrr = min(minIrr, irritated)
print minIrr
