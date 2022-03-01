import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def ni(): return int(inp())

MOD = 1000000007
T = ni()
for _ in range(T):
    d = ni()
    val = 8 * pow(9, d-1, MOD) % MOD
    print(val)