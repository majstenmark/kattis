import sys
DP = {}
def S(C, v):
    if C == 5:
        return (5, 0)
    if C in DP:
        return DP[C]
    e1, o1 = S(C//5, v^1)
    if v==0:
        DP[C] = e1*3 + o1*2, e1*2 + o1*3
    else:
        DP[C] = e1*5, o1*5
    return DP[C]

def solve(N, C, v):
    if N < 0:
        print(N, C, v)

    if N <= 5:
        return N, 0
    if N < C:
        return solve(N, C//5, v^1)
    else:
        e1, o1 = solve(N-C, C, v)
        e2, o2 = S(C, v)
        if v==1:
            return e2 + o1, o2 + e1
        else:
            return e2 + e1, o2 + o1
while True:
    N = input()
    if N == -1: break
    C = 1
    v = 1
    while C <= N:
        C *= 5
        v ^= 1
    print solve(N+1, C//5, v)[0]
