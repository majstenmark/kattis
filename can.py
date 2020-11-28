n =  int(raw_input())
coins = [int(v) for v in raw_input().split()] # sorted
S = coins[-1] + coins[-2]
allowedCoins = [0 for _ in range(S)]
coinIndex = 0
for v in range(S):
    while coinIndex+1 < n and coins[coinIndex+1] <= v:
        coinIndex+=1
    allowedCoins[v]=coinIndex
#print(allowedCoins)
greedy = [0 for _ in range(S)]
opt = [x for x in range(S)]
for v in range(1, S):
    greedy[v] = 1 + greedy[v-coins[allowedCoins[v]]]

    for i in range(allowedCoins[v]+1):
        c  = coins[i]
        test  = 1  + opt[v-c]
        opt[v] = min(opt[v],test)
    if opt[v] < greedy[v]:
#        s='Value {} greedy {} and opt {}'.format(v,greedy[v], opt[v])
#        print(s)
        print('non-canonical')
        exit()
#print('greedy ' + str(greedy))
#print('opt ' + str(opt))
print('canonical')
