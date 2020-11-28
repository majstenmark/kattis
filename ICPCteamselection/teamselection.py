D = int(raw_input())
for d in range(D):
    N = int(raw_input())
    teams = sorted(map(int, raw_input().split()))
    S = 0
    for i in range(N, 3*N, 2):
        S += teams[i]
    print(S)
