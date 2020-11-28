def solve(l1, a1, l2, a2,lt, at):
    sol = '?'
    first = True
    for test1 in range(1, 10001):
        test2 = (lt - l1*test1)/l2
        resL = test1*l1 + test2*l2
        resA = test2*a2 + a1*test1
        if resA == at and resL == lt and test2 > 0:
            if first:
                sol = '{} {}'.format(test1, test2)
                first = False
            else:
                return '?'
    return sol

N = int(raw_input())
for n in range(N):
    l1, a1, l2, a2,lt, at = map(int, raw_input().split())
    print(solve(l1, a1, l2, a2,lt, at))
