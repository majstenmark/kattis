import sys
from fractions import Fraction

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def ni(): return int(inp())

TOT = 2**20 + 10
isPrime = [1] * TOT
primes = set()
for p in range(2, TOT):
    if isPrime[p]:
        primes.add(p)
        for k in range(p*p, TOT, p):
            isPrime[k] = 0

def isAPrime(n):
    if n < 2: return False
    if n in primes: return True
    for p in primes:
        if n%p == 0: return False
    return True

def toint(s, base):
    try:
        v = int(s,base)
        return True, isAPrime(v)
    except:
        return False, 0

T = ni()
bases = [2, 8, 10, 16]
for _ in range(T):
    s = inp()
    ok_bases = 0
    no_primes = 0
    for base in bases:
        ok, prime = toint(s, base)
        if ok:
            ok_bases += 1
            if prime:
                no_primes += 1
    f = Fraction(no_primes, ok_bases)
    print(f'{f.numerator}/{f.denominator}')
