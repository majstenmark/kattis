L, N = [int(v) for v in raw_input().split()]
k = 1
n = N
r= L%N
while r != 0:
    n = n - r
    r = L % n
    k += 1
print(k)