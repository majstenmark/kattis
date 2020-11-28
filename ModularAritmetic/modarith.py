
# returns g = gcd(a, b), x0, y0,
# where g = x0*a + y0*b
def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = (a // b, b, a % b)
        x0, x1 = (x1, x0 - q * x1)
        y0, y1 = (y1, y0 - q * y1)
    return (a, x0, y0)

def doshit(x, y, N):
    g, a, b = xgcd(y, N)
    if g !=1:
        return -1
    return (x * a) % N

N, T = map(int, raw_input().split())
while not (N == 0 and T == 0):
    for t in range(T):
        line = raw_input()
        if '/' in line:
            x, y = map(int, line.split('/'))
            print(doshit(x,y, N))
        else:
            print(eval('('+line+') %' + str(N)))

    N, T = map(int, raw_input().split())
