def solve(n, k):
    period = 2 ** n
    if (K  + 1) % period == 0:
        return True
    return False            
    

T = int(raw_input())
for t in range(T):
    N, K =[int(v) for v in raw_input().split()]
    res = solve(N, K)
    ans = 'ON' if res else 'OFF'
    print('Case #{}: {}'.format(t+1, ans))