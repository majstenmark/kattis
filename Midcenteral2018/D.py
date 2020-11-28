R = 'A23456789TJQK'
rank = {x: index for index, x in enumerate(R)}
cnt = [0] * len(R)

cards = raw_input().split()
for card in cards:
    cnt[rank[card[0]]] += 1
print max(cnt)
