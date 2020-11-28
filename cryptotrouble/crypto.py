
def solve(N, B):
    B = map(int, B)
    MOD = 10 ** 9 + 7
    table = [[0, 0, 0] for _ in range(N + 1)] # mod 0, mod 1 mod 2, leadingzeros
    #zeros = [[0, 0, 0] for _ in range(N + 1)] # mod 0, mod 1 mod 2, leadingzeros
    zcnt = 0

    for n in range(N-1, -1, -1):
        dig = B[n] % 3
        if B[n] == 0:
            zcnt += 1
            #leading zeros
            """
            zeros[n] = [(2*zeros[n+1][0] + table[n+1][0])  % MOD, 
            (2* zeros[n+1][1] + table[n+1][1])  % MOD, 
            (2 * zeros[n+1][2] + table[n+1][2])  % MOD]
            zeros[n][0] +=1
            zeros[n][0] %= MOD
            table[n] = table[n+1]
           
            """
            
        #else:
       # zeros[n] = zeros[n+1]
        
        mod0 = (table[n+1][0]+ 
        table[n+1][(- dig) % 3])% MOD

        mod1 = (table[n+1][1]+
        table[n+1][(1 - dig) % 3]) % MOD

        mod2 = (table[n+1][2] +
        table[n+1][(2 - dig) % 3]) % MOD

        table[n] = [mod0, mod1, mod2]
        table[n][dig] += 1 
        table[n][dig] %= MOD
    #print(table)
    #print(zeros)

    cnt = table[0][0] - 2**(zcnt) + 1
    cnt %= MOD

    return cnt

if __name__ == '__main__':
    N = int(raw_input())
    B = raw_input()
    print(solve(N, B))
