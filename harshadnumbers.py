def dig_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n/10
    return s

N = int(raw_input())
for nbr in range(N, 1000000001):
    ds = dig_sum(nbr)
    if nbr % ds == 0:
        print(nbr)
        exit()
