N = int(input())
digits = [int(input()) for _ in range(N)]
reverse = map(str, digits[::-1])
print('\n'.join(reverse))
