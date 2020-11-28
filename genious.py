inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

pairs = [1, 0, 3, 2]
others = {0: [2, 3], 1:[2, 3], 2: [0, 1], 3: [0, 1]}

def wins(pl, ws):
    #wins his own game
    A = ws[pl]
    B = ws[pairs[pl]]
    a_wins = A /(A + B)
    
    #c wins
    oth = others[pl]
    C = ws[oth[0]]
    D = ws[oth[1]]

    #meets C
    c_wins = C/(C+D)
    ac_wins = A/(C+A)

    d_wins = D/(C + D)
    ad_wins = A/(D + A)

    win = a_wins * c_wins * ac_wins + a_wins * d_wins * ad_wins
    return win




K, T, P, Q, X1 = nl()
X = X1
prob_wins = []
for _ in range(T):
    ws = nl()

    winner = X % 4
    prob_is_winner = wins(winner, ws)
    prob_wins.append(prob_is_winner)

    X = (X * P) % Q

#print(prob_wins) 
DP = [1.0]
for t in range(T):
    nxt = [0] * (t+2)
    for k, p in enumerate(DP):
        prob = prob_wins[t]
        #if winner
        nxt[k+1] += p * prob

        #loss
        nxt[k] += p * (1-prob)
    DP = nxt
su = 0
#print(DP)
for k in range(K, len(DP)):
    su += DP[k]
    
print(su)