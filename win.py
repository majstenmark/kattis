def solve(adj, N, M):
    INF = 10**12
    val = [(INF, -INF)] * N
    nextval = [(INF, -INF)] * N
    val[0] = (0, 0)
    g = [[] for _ in range(N)]
    for i, row in enumerate(adj):
        for j, col in enumerate(row):
            g[j].append((i, col))

    for turn in range(M):
        for node in range(N):
            minval = INF
            maxval = - INF
            for ne, winning in g[node]:
                minval = min(minval, val[ne][0] + winning)
                maxval = max(maxval, val[ne][1] + winning)
            nextval[node] = (minval, maxval)
        #print(nextval)
        val, nextval = nextval, val
    mi = INF
    mx = -INF
    for minval, maxval in val:
        mi = min(mi, minval)
        mx = max(mx, maxval)
    return mi, mx
    


N = int(raw_input())
while N > 0:
    adj = []
    for n in range(N):
        line = [int(v) for v in raw_input().split()]
        adj.append(line)
    M = int(raw_input())
    mi, mx = solve(adj, N, M)
    print('{} {}'.format(mx, mi))

    N = int(raw_input())
