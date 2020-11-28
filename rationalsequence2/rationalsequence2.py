import re

tests = int(input())
def f(p, q):
    if p == 1 and q == 1:
        return 1
    if p > q:
        return 2*f(p - q, q) +1
    return 2* f(p, q - p)
for t in range(tests):
    testid, p, q = map(int, re.split(' |/', input()))
    print(testid, f(p, q))
