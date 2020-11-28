T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    v1 = [int(v) for v in raw_input().split()]
    v2 = [int(v) for v in raw_input().split()]
    v1.sort()
    v2.sort(reverse =  True)

    res = 0
    for n in range(N):
        res += v1[n]*v2[n]

    print('Case #{}: {}'.format(t+1, res))
