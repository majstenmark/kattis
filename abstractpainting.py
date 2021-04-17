MOD = 10**9 + 7
def solve(R, C):
    S = pow(3, R)
    M = 3*pow(2, R)
    return S*pow(M, C, MOD)%MOD

T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    print(solve(R,C))