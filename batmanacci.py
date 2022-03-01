N, K = map(int, input().split())

fib = [0, 1, 1]
for i in range(2, N):
    f = fib[-1] + fib[-2]
    fib.append(f)
k = K
n = N
while n > 2:
    #print(f'k = {k} n = {n}')
    lo = fib[n-2]
    hi = fib[n-1]
    if k > lo:
        k -= lo
        n = n-1
    else:
        n = n- 2
if n == 1:
    print('N')
else:
    print('A')

