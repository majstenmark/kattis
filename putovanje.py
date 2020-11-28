def eat(W, i):
    w = 0
    cnt = 0
    for ii in range(i, N):
        if w + W[ii] <= C:
            w += W[ii]
            cnt += 1
        
    return cnt

N, C = [int(v) for v in raw_input().split()]
W = [int(v) for v in raw_input().split()]
max_fruits = 0
for n in range(N):
    alt = eat(W, n)
    max_fruits = max(max_fruits, alt)
print(max_fruits)