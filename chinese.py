# returns g = gcd(a, b), x0, y0,
# where g = x0*a + y0*b
def xgcd(a, b):
    x0, x1, y0, y1 = 1,0,0,1
    while b !=0:
        q, a, b = (a // b, b, a % b)
        x0, x1 = (x1, x0 - q * x1)
        y0, y1 = (y1, y0 - q * y1)
    return (a, x0, y0)

def lcm(a, b):
    g, u, v = xgcd(a, b)
    return g, u, v, a*b/g


T = int(raw_input())
no_sol = 'no solution'
for t in range(T):
    A, M, B, N = map(int, raw_input().split())
    g, u, v, K = lcm(M, N)
    if A % g == B % g:
        x = ((A *v *N + B * u * M)/g) % K
        print('{} {}'.format(x, K))

    else:
        print(no_sol)
# 1514746 2002000
