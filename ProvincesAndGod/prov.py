G, S, C = map(int, raw_input().split())
worth = [3, 2, 1]
value = G * worth[0] + S * worth[1] + C * worth[2]
vict = [('Province', 8), ('Duchy', 5), ('Estate', 2)]
tres = [('Gold', 6), ('Silver', 3), ('Copper', 0)]
vi = ''
t = 'Copper'
for v, c in vict:
    if value >= c:
        vi = v
        break
for v, c in tres:
    if value >= c:
        t = v
        break
if vi:
    print '{} or {}'.format(vi, t)
else:
    print t
