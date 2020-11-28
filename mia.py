def score(d1, d2):
    v = 10 * d1 + d2
    if v == 12 or v == 21:
        return 1000
    if d1 == d2:
        return 100 * d1 + 10 * d2
    mx, mn = max(d1, d2), min(d1, d2)
    return 10 * mx+ mn

s0, s1, r0, r1 = [int(v) for v in raw_input().split()]
while (s0, s1, r0, r1) != (0, 0, 0, 0):
    score1= score(s0, s1)
    score2 = score(r0, r1)
    if score1 == score2:
        print('Tie.')
    else:
        winner = 1 if score1 > score2 else 2
        print('Player {} wins.'.format(winner))

    s0, s1, r0, r1 = [int(v) for v in raw_input().split()]
    