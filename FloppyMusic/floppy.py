def check(T, intervals):
    states = [[False] * T for _ in range(len(intervals)+1)]
    for state in range(T):
        states[0][state] = True
    for i,il in enumerate(intervals):
        some = False
        for ins, s in enumerate(states[i]):
            if s:
                if ins + il < T:
                    states[i+1][ins + il] = True
                    some = True

                if ins - il >= 0:
                    states[i+1][ins - il] = True
                    some = True

        if not some:
            return False
    return True


F = input()
for f in range(F):
    T, N = map(int, raw_input().split())
    intervals = []
    for n in range(N):
        t1, t2 = map(int, raw_input().split())
        intervals.append(t2 - t1)
    ok = check(T+1, intervals)
    if not ok:
        print 'impossible'
        exit()
print 'possible'
