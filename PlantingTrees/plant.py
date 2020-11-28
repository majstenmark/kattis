N = input()
Ti = map(lambda x:int(x) +1, raw_input().split())
Ti.sort(reverse = True)
party = 1
for index, tree in enumerate(Ti):
    day = index + 1
    party = max(party, day + tree)
print party
