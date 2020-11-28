inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

INF = 10**12
n, m = nl()
while n != 0:
    offers = [nl() for _ in range(n)]
    best = 0, INF #no tickets, for inf price

    for tickets, price in offers:
        if tickets <= m:
            if price * best[0] < tickets * best[1]:
                best = tickets, price
            if price * best[0] == tickets * best[1] and tickets > best[0]:
                best = tickets, price
                
    if best[0] == 0:
        print('No suitable tickets offered')
    else:
        print('Buy {} tickets for ${}'.format(best[0], best[1]))

    n, m = nl()
