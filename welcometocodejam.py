from collections import defaultdict as dd

welcome = 'welcome to code jam'
ind = dd(list)

for i, lt in enumerate(welcome):
    ind[lt].append(i)


def solve(s):
    cnt = [0] * (len(welcome) +1)
    cnt[0] = 1
    for lt in s:
        if lt in ind:
            indeces = ind[lt]
            for i in indeces:
                cnt[i+1] += cnt[i]
                cnt[i+1] %= 10000
    result = str(cnt[-1])
    return '0' * (4-len(result)) + result
    


T = int(raw_input())
for t in range(T):
    S = raw_input()
    res = solve(S)
    print('Case #{}: {}'.format(t+1, res))