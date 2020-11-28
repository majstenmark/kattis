N, Q = map(int, raw_input().split())
X = map(int, raw_input().split())
for _ in range(Q):
    a, b, c = map(int, raw_input().split())
    if a == 1:
        X[b-1] = c
    else:
        print(abs(X[b-1] - X[c-1]))
