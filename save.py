N, D = [int(v) for v in raw_input().split()]
p = [int(v) for v in raw_input().split()]
INF = 10**12
earnings = [[[-INF for r in range(10)] for d in range(D+1)] for i in range(N+1  )]
earnings[0][0][0] = 0
initsum = sum(p)

def gains(r):
    if r < 5:
        return r
    return r-10

for i in range(1, N+1):
    price = p[i-1]
    for d in range(D+1):
        for r in range(10):
            #no bar
            earnings[i][d][(r + price)%10] = max(earnings[i][d][(r + price)%10], earnings[i-1][d][r])
            #bar
            if d == D: continue
            earnings[i][d +1][price%10] = max(earnings[i][d +1][price%10], earnings[i-1][d][r] + gains(r))

maxearned = -INF
for d in range(D+1):
    for r in range(10):
        alt = earnings[-1][d][r] + gains(r)
        maxearned = max(alt, maxearned)

endprice = initsum - maxearned
print(endprice)