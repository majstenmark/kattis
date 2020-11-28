from random import random, randint as ri
k = 16
n = 100
print(k, n)
for _ in range(n):
    print(random(), ri(1, (1<<k)-1))
