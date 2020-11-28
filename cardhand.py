from itertools import permutations
def minMoves(ws, N):
    inc = [1 for w in ws]# start
    for t in range(1, N):
        for b in range(0,t):
            if ws[b] < ws[t] and inc[t] <= inc[b]:
                inc[t]= inc[b] + 1
    return N - max(inc)

def rank(ch):
    if ch == 'T':
        return 10
    if ch == 'J':
        return 11
    if ch == 'Q':
        return 12
    if ch == 'K':
        return 13
    if ch == 'A':
        return 14
    return int(ch)



def calcScore(suitPerm, dirs, cards):
    vals = {}
    for index, suit in enumerate(suitPerm):
        vals[suit] = (index * 20, dirs[index])
    ws = []
    for card in cards:
        r = rank(card[0])
        v, d = vals[card[1]]
        score = v
        if d == '1':
            score += (14 - r)
        else:
            score += r
        ws.append(score)
    return ws


N = int(raw_input())
cards = raw_input().split()
suits = ['h', 'c', 'd', 's']
suitPerms = permutations(suits)
moves = N
for p in suitPerms:
    for dir in range(16):
        bi = bin(dir)[2:]
        ws = calcScore(p, '0'* (4 - len(bi)) + bi, cards)
        neededMoves = minMoves(ws, N)
        moves = min(moves, neededMoves)
print moves
