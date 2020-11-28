def comp(state1, state2):
    if state1 + state2 == 3:
        return False
    return True 


def solve(N, K):
    vals = []
    for n in range(N):
        l, r = [int(v) for v in raw_input().split()]
        vals.append([l, r])
    #DP over N, k, state, stores maximum value 
    NONE = 0
    LEFT = 1
    RIGHT = 2
    def printmatrix(m):
        for n in range(N+1):
            print(m[n])
    INF = 10**12

    dp = [[[-INF for _ in range(0, 3)] for _ in range(K+1)] for _ in range(N+1)]


    dp[0][0][NONE] = 0
    

    if K == 0:
        s = 0
        for i in range(N):
            s += sum(vals[i])
        print(s)
        return 

    for i in range(0, N):
        for k in range(K+1):
            #NONE
            NONE_add = sum(vals[i])
            LEFT_add = vals[i][0]
            RIGHT_add = vals[i][1]

            # i+1 i DP motsvarar rad i
            dp[i+1][k][NONE] = max(dp[i+1][k][NONE], 
            dp[i][k][NONE] + NONE_add)

            dp[i+1][k][NONE] = max(dp[i+1][k][NONE], 
            dp[i][k][LEFT] + NONE_add)


            dp[i+1][k][NONE] = max(dp[i+1][k][NONE], 
            dp[i][k][RIGHT] + NONE_add)

            if k < K:

                dp[i+1][k+1][RIGHT] = max(dp[i+1][k+1][RIGHT], 
                dp[i][k][RIGHT] + RIGHT_add)

                dp[i+1][k+1][LEFT] = max(dp[i+1][k+1][LEFT], 
                dp[i][k][NONE] + LEFT_add)
                
                dp[i+1][k+1][RIGHT] = max(dp[i+1][k+1][RIGHT], 
                dp[i][k][NONE] + RIGHT_add)

                dp[i+1][k+1][LEFT] = max(dp[i+1][k+1][LEFT], 
                dp[i][k][LEFT] + LEFT_add)

    best = 0
    # printmatrix(dp)
    for state in range(NONE, RIGHT + 1):
        best = max(best, dp[N][K][state])
    print(best)

while True:
    N, K = [int(v) for v in raw_input().split()]
    if N == K == 0:
        exit()
    solve(N, K)
