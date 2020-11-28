def in_trinagle(n, N):
    
    for nb1, v1 in enumerate(g[n]):
        for nb2, v2 in enumerate(g[n]):
            
            if v1 > 0 and v2 > 0 and g[nb1][nb2] > 0:
                return True
    return False

N = int(raw_input())
while N != -1:
    g = [[] for _ in range(N)]
    for n in range(N):
        row = [int(v) for v in raw_input().split()]
        g[n] = row
    weak =[]
    for n in range(N):
       if not in_trinagle(n, N):
           
           weak.append(str(n))
    print(' '.join(weak))

    N = int(raw_input())
    