N, Dm = map(int, raw_input().split())
days = map(int, raw_input().split())
cnt = 0
for n in range(N):
    if days[n] <= Dm:
        break
    cnt+=  1
if cnt == N:
    print "It had never snowed this early!"
else:
    print "It hadn't snowed this early in {} years!".format(cnt)
