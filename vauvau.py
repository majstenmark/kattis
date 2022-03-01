def nl(): return [int(v) for v in input().split()]

def check(ang, calm, time):
    k = ang + calm
    t = time % k
    if 0 < t <= ang:
        return 1
    return 0

A, B, C, D = nl()
arr = nl()
for t in arr:
    cnt = check(A, B, t) + check(C, D, t)
    if cnt == 0:
        print('none')
    elif cnt == 1:
        print('one')
    else:
        print('both')
