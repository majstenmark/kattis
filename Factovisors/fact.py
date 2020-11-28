import math
import sys

def primes(m):
    prims = {}
    for p in range(2, int(math.sqrt(m)+2)):
        if m % p == 0:
            k = 0
            while m % p == 0:
                m /= p
                k += 1
            prims[p] = k
    if m > 1:
        prims[m] = 1
    return prims

def check(A, B):
    if B == 0:
        return False
    for p, alpha in primes(B).items():
        c = 0
        n = A
        while n > 0:
            c += n/p
            n /= p
        if c < alpha:
            return False
    return True

for line in sys.stdin:
    A, B = map(int, line.split())
    if check(A, B):
        print "{} divides {}!".format(B, A)
    else:
        print "{} does not divide {}!".format(B, A)
