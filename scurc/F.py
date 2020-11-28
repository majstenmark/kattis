T = input()
for _ in range(T):
    N = input()
    from collections import *
    C = Counter()
    for _ in range(N):
        n, i = raw_input().split()
        C[n] += int(i)
    out = sorted(C.items(), key=lambda x: (-x[1], x[0]))
    print(len(out))
    print('\n'.join(map(lambda x: '{} {}'.format(*x), out)))
