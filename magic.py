N, K, T = map(int, raw_input().split())

amount = [[0] * (N+1) for _ in range(T+1)]
amount[0][0] = 1
MOD = 1000000009
for i in range(N):
    for card in range(1, K+1):
        for t in range(T+1):
            if t + card <= T:
                amount[t + card][i + 1] += amount[t][i]
                amount[t + card][i + 1] %= MOD
print amount[T][N]
