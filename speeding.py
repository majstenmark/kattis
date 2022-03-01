N = int(input())
tot = 0
prev = 0
mx = 0
for _ in range(N):
    t, d = map(int, input().split())
    diff = d - tot
    dt = t - prev
    if (dt > 0):
        speed = diff/dt
        mx = max(mx, speed)
    prev = t
    tot = d
print(int(mx))
