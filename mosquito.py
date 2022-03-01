import sys
lines = sys.stdin.readlines()


def sim(M, P, L, E, R, S, N ):
    for _ in range(N):
        new_P = L//R
        new_M = P//S
        new_L = M * E
        P = new_P
        M = new_M
        L = new_L
    return M


for line in lines:
    M, P, L, E, R, S, N = map(int, line.split())
    print(sim(M, P, L, E, R, S, N))