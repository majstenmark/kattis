from collections import defaultdict as dd

def primes(x):
    N = int(X ** 0.5) + 10
    sieve = [True] * N
    sieve[0] = False
    sieve[1] = False
    for i in range(2, N):
        for j in range(i * i, N,i):
           sieve[j] = False 
    cnt = 0
    left = x
    for i in range(2, min(N, x)):
        if sieve[i]:
            c = i
            while x % c == 0:
                cnt += 1
                left /= i
                c*= i
    if left > 1:
        cnt += 1
    return max(cnt,1)

X= int(raw_input())
k =primes(X)

print(k)