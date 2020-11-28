N, K = map(int, raw_input().split())
safe = [False] * N
for k in range(K):
    S = int(raw_input())
    safe[S-1] = True
tot = N * (N +1)/2
#print 'tot', tot
unsafe = 0
for n in range(N):
    if not safe[n]:
        unsafe += 1
    if (safe[n] or n == N -1) and unsafe > 0:
        tot -= unsafe * (unsafe + 1)/2
    #    print 'unsafe ', unsafe
        unsafe = 0

print tot
