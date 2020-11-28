N, M = [int(v) for v in raw_input().split()]
if N == M-1:
    print('Dr. Chaz will have 1 piece of chicken left over!')
elif N == M + 1:
    print('Dr. Chaz needs 1 more piece of chicken!')
elif N < M:
    print('Dr. Chaz will have {} pieces of chicken left over!'.format(M -N))
else:
    print('Dr. Chaz needs {} more pieces of chicken!'.format(N -M))