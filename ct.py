N,T,K = map(int,raw_input().split())
cards = map(int, raw_input().split())
pairs= [0 for _ in range(T)]
for c in cards:
    pairs[c - 1] += 1
price_per_pair = [0 for _ in range(T)]
anthonys_money = 0
for t in range(T):
    a,b= map(int, raw_input().split())
    price_per_pair[t] = (2 - pairs[t]) * a +pairs[t] * b
    anthonys_money += pairs[t] * b
price_per_pair.sort()
total_profit = anthonys_money
for k in range(K):
    total_profit -= price_per_pair[k]
print(total_profit)
