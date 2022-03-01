import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def solve(R, S, X, Y, W):
    if W <= 1: return False
    r = S - R + 1
    P = [[0] * (Y+1) for _ in range(Y+1)]
    P[0][0] = 1.0
    p1 = (R-1)/S
    p2 = (S-R+1)/S

    for n in range(1, Y+1):
        for k in range(0, n+1):
            P[n][k] = p1 * P[n-1][k] + p2 * P[n-1][k-1]
    win = 0
    for k in range(X, Y+1):
        win += P[Y][k]
    return W * win > 1

        
N = ni()
for _ in range(N):
    R, S, X, Y, W = nl()
    print('yes' if solve(R, S, X, Y, W) else 'no')

