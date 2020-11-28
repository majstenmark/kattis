T = input()
for _ in range(T):
    N = input()
    v = 1
    for i in range(1, N+1):
        v *= i
    print(v%10)

