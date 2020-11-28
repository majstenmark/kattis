H = map(int, raw_input().split())[1:]
B = map(int, raw_input().split())[1:]

INF = 10**12
buns =[[INF] * 1001 for _ in range(len(B))]
hotdogs = [[INF] * 1001 for _ in range(len(H))]

for n in range(len(H)):
    hotdogs[n][0] = 0
for n in range(len(B)):    
    buns[n][0] = 0

for index,pack in enumerate(H):
    for nbr in range(len(buns)):
        if buns[nbr] < INF:
            buns[nbr + pack] = min(buns[nbr + pack], buns[nbr] + 1)

for index,pack in enumerate(H):
    for nbr in range(len(hotdogs)):
        if hotdogs[nbr] < INF:
            hotdogs[nbr + pack] = min(hotdogs[nbr + pack], hotdogs[nbr] + 1)
min_pack = INF
for index in range(len(bund)):
    if buns[index] < INF and hotdogs[index] <INF:
        alt = buns[index] + hotdogs[index]
        min_pack= min(alt, min_pack)

if min_pack< INF:

    print(min_pack)
else:
    print('impossible')
