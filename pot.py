N = int(raw_input())
P = [int(raw_input()) for n in range(N)]
X= 0
for n in range(N):
    p = P[n]
    exp = p % 10
    num = p//10
    X += num ** exp
print(X)