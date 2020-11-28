from itertools import permutations

def isSet(p):
    s = [set() for _ in range(4)]
    for i in range(4):
        for c in p:
            card =cards[c]
            s[i].add(card[i])
    for t in s:
        if len(t) == 2:
            return False
    return True
            

cards = []
for _ in range(4):
    line = raw_input().split()
    cards.extend(line)

found =set()
sets = []

for perm in permutations(range(12), 3):
    T = tuple(sorted(perm))
    if isSet(T):
        found.add(T)
sets= list(found)
sets.sort()
for s1, s2, s3 in sets:
    print('{} {} {}'.format(s1+1, s2+1, s3+1)) 
if len(sets) == 0:
    print('no sets')
