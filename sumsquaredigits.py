def solve(b, n):
    a = []
    while n > 0:
        ai = n % b
        n = n//b
        a.append(ai)
    su = 0
    for ai in a:
        su += ai **2
    return su

P = int(raw_input())
for p in range(P):
    K, b, n = [int(v) for v in raw_input().split()]
    res = solve(b, n)
    print('{} {}'.format(K, res))