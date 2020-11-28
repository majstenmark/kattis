N = int(raw_input())
while N > 0:
    fixed = [int(raw_input()) for _ in range(N)]
    unsync = [int(raw_input()) for _ in range(N)]
    orig1 = sorted(fixed)
    orig2 = sorted(unsync)
    match = {}
    for n in range(N):
        match[orig1[n]] = orig2[n]
    out = []
    for n in range(N):
        out.append(match[fixed[n]])
    print('\n'.join(map(str, out)))
    print('')
    N = int(raw_input())