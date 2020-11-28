N =int(raw_input())
for n in range(N):
    a = int(raw_input())
    print(str(a) + ' is odd' if a % 2 == 1 else str(a) + ' is even')