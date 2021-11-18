N = int(input())

def ask(li):
    out = ['?', str(len(li))]
    for v in li:
        out.append(str(v+1))
    print(' '.join(out), flush = True)
    return int(input())


adj = [[0] * N for _ in range(N)]
outgoing = [0] * N
for i in range(N):
    res = ask([i])
    outgoing[i] = res
for i in range(N):
    for j in range(i+1, N):
        res = ask([i, j])
        tot = outgoing[i] + outgoing[j]
        if res < tot:
            adj[i][j] = 1
            adj[j][i] = 1

out = ['!']
for r in range(N):
    out.append(' '.join(map(str, adj[r])))  
print('\n'.join(out))
