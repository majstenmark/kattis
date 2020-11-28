import sys

def cover(intervals, A, B):
    intervals.sort()
    active = []
    used = []
    a = A
    index = 0
    while index < len(intervals):
        s, e, i = intervals[index]
        index += 1
        if s <= a:
            active.append((s, e, i))
        else:
            # pick one

            if len(active) > 0:
                for best in active: break

                for ss, ee, ii in active:
                    if ee > best[1]:
                        best = (ss, ee, ii)

                used.append(best[2])
                a = best[1]
                if a >= B:
                    return used

            else:
                # no interval covers a
                return []
            active = []
            index -= 1

    if len(active) > 0:
        for best in active: break

        for ss, ee, ii in active:
            if ee > best[1]:
                best = (ss, ee, ii)
        used.append(best[2])
        a = best[1]
        if a >= B:
            return used
    return []

line = sys.stdin.readline()
while line:
    A, B = map(float, line.split())
    N =int(sys.stdin.readline())
    intervals = []
    for n in range(N):
        a, b = map(float, sys.stdin.readline().split())
        intervals.append((a, b, n))
    res = cover(intervals, A, B)
    if len(res) == 0:
        print 'impossible'
    else:
        print len(res)
        s = ' '.join(map(str, res))
        print s
    line = sys.stdin.readline()
