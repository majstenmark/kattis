def nl():
    return [int(v) for v in raw_input().split()]

def ni():
    return int(raw_input())

S, P, M, N = nl()
times = nl()
INF = 10**18
DP = [INF] * (N+1)
DP[0] = 0
next = 0
for i in range(N):
    #buy single
    DP[i+1] = min(DP[i+1], S + DP[i])
    #buy period
    while next < N and times[next] < times[i] + M:
        next += 1
    DP[next] = min(DP[next], P + DP[i])
print(DP[-1])
