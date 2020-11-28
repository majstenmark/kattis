S = input()

cards = set()
suits = {s:set() for s in ['P', 'K', 'H', 'T']}
for c in range(0, len(S), 3):
    cc = S[c: c + 3]
    if cc in cards:
        print('GRESKA')
        exit()
    cards.add(cc)
    suits[cc[0]].add(cc)
missing = [str(13 - len(suits[s])) for s in ['P', 'K', 'H', 'T']]
print(' '.join(missing))
    
