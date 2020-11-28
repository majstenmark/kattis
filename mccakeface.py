from collections import Counter

cnt= Counter()
N = input()
M = input()
Ns = map(int, raw_input().split())
Ms = map(int, raw_input().split())
for n in xrange(N):
    for m in xrange(M):
        i = Ms[m] - Ns[n]
        if i >= 0:
            cnt[i] += 1
MAX= 0
ct = 0
for time, count in cnt.items():
    if count > MAX:
        MAX = count
        ct = time
    if count == MAX:
        ct = min(time, ct)
print ct
