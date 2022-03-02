import sys
import math
sys.setrecursionlimit(1000)

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

 
def ds(n):
    s = str(n)
    d = len(s) - 1
    d = max(d, 1)
    dp = [0]*(d + 1)
    dp[0] = 0
    dp[1] = 9 * 10//2
    for i in range(2, d + 1):
        dp[i] = dp[i - 1] * 10 + dp[1] * 10**(i - 1)
         
    return ds_helper(n, dp)

 
def ds_helper(n, dp):
    if (n < 10):
        return (n * (n + 1)) // 2
    s = str(n) 
    d = len(s) - 1
    p = 10**d
    biggest = n // p
    return (biggest * dp[d] + (biggest * (biggest - 1) // 2) * p + biggest * (1 + n % p) + ds_helper(n % p, dp))


T = ni()
out = []
for _ in range(T):
    a, b = nl()
    out.append(ds(b) - ds(a-1))
print('\n'.join(map(str, out)))