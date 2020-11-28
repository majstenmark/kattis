T = int(raw_input())
tests = [int(raw_input()) for _ in range(T)]
maxN = max(3, max(tests) +1)
table = [[-1 for _ in range(maxN)] for _ in range(2)]
table[0][2] = 2
table[1][2] = 1
table[0][1] = 1
table[1][1] = 1
MOD = 10**9 +7
for n in range(3, maxN):
    # three options 00, 01, and 10
    table[0][n] = ((2 * table[0][n - 2])% MOD  + table[1][n - 2])% MOD
    table[1][n] = (table[0][n-2] + table[1][n-2]) % MOD
for test in tests:
    tot = (table[0][test] + table[1][test]) %MOD
    print(tot)
