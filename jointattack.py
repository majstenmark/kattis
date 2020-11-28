def gcd(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    return b if a % b == 0 else gcd(b, a % b)

N = int(raw_input())
xi = [int(v) for v in raw_input().split()]
taljare = 1
namnare = xi[-1]
for i in range(N-2, -1,-1):
    x = xi[i]
    taljare = x * namnare + taljare
    g = gcd(taljare, namnare)
    taljare = taljare// g
    namnare = namnare //g
    taljare, namnare = namnare, taljare
print('{}/{}'.format(namnare, taljare))
    