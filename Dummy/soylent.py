import math
b = 400
T = int(input())
for t in range(T):
    N = int(input())
    k = math.ceil(N/b)
    print(k)
