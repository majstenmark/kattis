from collections import defaultdict as dd

N = int(raw_input())
for n in range(N):
    G =int(raw_input())
    gs= [int(v) for v in raw_input().split()]
    cnt = dd(int)
    for i in gs:
        cnt[i] += 1
    odd = -1
    for i in gs:
        if cnt[i] == 1:
            print('Case #{}: {}'.format(n+1, i))
    