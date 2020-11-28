def xgcd(a, b):
  x0, x1, y0, y1 = 1, 0, 0, 1
  while b != 0:
    q, a, b = (a // b, b, a % b)
    x0, x1 = (x1, x0 - q * x1)
    y0, y1 = (y1, y0 - q * y1)
  return (a, x0, y0)

def modfac(u):
    kfac = 1
    for i in range(2, u+1):
        kfac *= i
        kfac %= MOD
    return kfac

def modchoose1(n, k):
    
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0    

def modchoose2(n, k):
    kfac = modfac(k)
    print('n {} k {}'.format(n,k))
    nkfac = modfac(n-k)
    print('nkfac', nkfac)
    knkfac = (kfac * nkfac) % MOD
    _, inv, _ = xgcd(knkfac, MOD)
    nfac = modfac(n)

    print('{} {} {} {}'.format(kfac, nkfac, knkfac, nfac))
    return inv * nfac % MOD

def modchoose3(n, k):
    k = min(k, n-k)
    to_remove = set(range(1, k+1))
    p = 1
    a = 0
    for i in range(n-k+1,n+1):
        if a%1000 == 0:
            cp = sorted(to_remove.copy(), reverse=True)
            print(a)
        a += 1
        for v in cp:
            if i%v == 0 and v in to_remove:
                i/=v
                to_remove.remove(v)
        p = p*i % MOD
    assert len(to_remove) == 0
    return p

"""

long modInverse(long a, long p) {
    //calculates the modular multiplicative of a mod m.
    //(assuming p is prime).
    return modPow(a, p-2, p);
}
long modBinomial(long n, long k, long p) {
// calculates C(n,k) mod p (assuming p is prime).

    long numerator = 1; // n * (n-1) * ... * (n-k+1)
    for (int i=0; i<k; i++) {
        numerator = (numerator * (n-i) ) % p;
    }

    long denominator = 1; // k!
    for (int i=1; i<=k; i++) {
        denominator = (denominator * i) % p;
    }

    // numerator / denominator mod p.
    return ( numerator* modInverse(denominator,p) ) % p;
}
"""
def modinv(a):
    return pow(a, p-2, p)

def modchoose(n, k):
    num = 1
    for i in xrange(k):
        num = num * (n - i)
    
    dem = 1
    for i in xrange(1, k + 1):
        dem = dem * i
    #print('{} {} {}'.format(num, dem , modinv(dem)))
    return num /dem % MOD

p = 10**9+7
MOD = 10**6+7
N, M , K = map(int, raw_input().split())
alls = modchoose(N + K -1, K)
inc_ex = K/(M + 1)
print('alls', alls)
cnt = alls 
for n in range(1, inc_ex + 1):
    kleft = K - n * (M+1)
    ways = modchoose(N, n)
    ai = modchoose(N + kleft -1, kleft)
    term = ((-1) ** n * ways * ai) % MOD
    cnt += term
    cnt %= MOD
print(cnt)
