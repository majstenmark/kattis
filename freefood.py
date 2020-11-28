N = int(raw_input())
free = [False]  * 366
for n in range(N):
    s,t = map(int, raw_input().split())
    for i in range(s, t + 1):
        free[i] = True
cnt = 0
for n in range(len(free)):
    cnt += 1 if free[n] else 0
print(cnt)