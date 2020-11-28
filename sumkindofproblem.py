P = int(raw_input())
for p in range(P):
    K, N = [int(v) for v in raw_input().split()]
    S1= (1 + N) * N //2
    S2= (1+ 2 *N-1)* N //2
    S3 = (2 + 2 * N) * N//2
    print('{} {} {} {}'.format(K, S1, S2, S3))
