nbr_of_days = int(raw_input())
prices = []
for d in range(nbr_of_days):
    prices.append(int(raw_input()))
money = 100
max_shares= 100000

shares = 0
for d in range(nbr_of_days - 1):
    if prices[d]<prices[d + 1] and shares == 0:
        # buy whole shares
        shares = min(money / prices[d], max_shares)
        money -= shares * prices[d]
    if prices[d]>prices[d + 1]:
        money += prices[d] * shares
        shares = 0
money += shares * prices[-1]
print(money)
