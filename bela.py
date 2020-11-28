table = {'A':(11, 11),
'K':(4, 4)
'Q': (3, 3),
'J':(20,2),
'T':(10, 10),
'9':(14, 0),
'8':(0,0),
'7':(0,0)}

Nstr, B = raw_input().split()
N = int(Nstr)
points = 0
for cards in range(4*N):
    c = raw_input()
    val = c[0]
    suit = c[1]
    if suit == B:
        points += table[val][0]
    else:
        points += table[val][1]
print(points)