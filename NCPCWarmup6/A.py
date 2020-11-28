inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def solve(N):
    used = [False] * N
    index = [i for i in range(N)]
    order = []
    step = 1
    curr = -1
    while len(order) < N:
        j = 0
        while j <= step:
            curr += 1
            curr %= N
            if not used[curr]:
                j += 1
        used[curr] = True
        order.append(curr)
        
        step += 1    
    
    out = [0]*N
    for i,v  in enumerate(order):
        out[v] = i+1

    return ' '.join(map(str, out))
        

T = ni()
for _ in range(T):
    N = ni()
    r= solve(N)
    print(r) 