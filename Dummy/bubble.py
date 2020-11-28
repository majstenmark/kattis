N =int(raw_input())
tea_prices=map(int, raw_input().split())
M = int(raw_input())
topping_prices=map(int, raw_input().split())
cheapest = 10 ** 12
for n in range(N):
    comb= map(int, raw_input().split())[1::]
    tea_price=tea_prices[n]
    for topping in comb:
        top_price = topping_prices[topping -1]
       # print('topping price', top_price)
        
        cheapest = min(cheapest, tea_price+ top_price)
X = int(raw_input())
#print(cheapest)
cups = X/cheapest
print(max(cups -1, 0))