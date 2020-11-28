def solve(n, d):
    whole = n//d
    rest = n % d
    print('{} {} / {}'.format(whole, rest, d))    

N, D = [int(v) for v in raw_input().split()]
while (N, D) != (0, 0):
    solve(N, D)
    N, D = [int(v) for v in raw_input().split()]