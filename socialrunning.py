N = int(input())
dist = [int(input()) for _ in range(N)]
best = 10 ** 30
for i in range(N):
    alt = dist[i] + dist[i-2]
    best = min(best, alt)
print(best)