import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

T = ni()
for _ in range(T):
    seats = 150+1
    N = ni()

    parties = [nl() for _ in range(N)]
    DP = [[0]*seats for _ in range(N+1)]
    DP[0][0] = 1
    
    for i in range(1, N+1):
        si, pi = parties[i-1]
        for s in range(seats):
            alt1 = 0
            if s >= si:
                p_best = DP[i-1][s-si]
                alt1 = p_best * pi/100
            alt2 = DP[i-1][s]
            DP[i][s] = max(DP[i][s], alt1, alt2)
    mx = max(DP[N][76:]) * 100
    print(mx)
        