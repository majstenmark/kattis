P = int(raw_input())
for p in range(P):
    K, N = [int(v) for v in raw_input().split()]
    tot = N + (1+ N) * N/2
    print('{} {}'.format(K,tot))