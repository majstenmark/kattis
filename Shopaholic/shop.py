N = input()
prices = map(int, raw_input().split())
prices.sort(reverse = True)

if N <= 2:
    print '0'
else:
    disc = 0
    for p in range(2, N, 3):
        disc += prices[p]
    print disc
