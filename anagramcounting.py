import sys
from collections import Counter

words = sys.stdin.read().strip().split('\n')
mx = max([len(w) for w in words])
N = mx+1
ft = [1] * N
for f in range(1, N):
    ft[f] = ft[f-1] * f
for w in words:
    L = len(w)
    all_comb = ft[L]
    cnt = Counter()
    for ch in w:
        cnt[ch] += 1
    F = 1
    for ch, i in cnt.items():
        f = ft[i]
        F *= f
    all_comb = all_comb // F
    print(all_comb)
