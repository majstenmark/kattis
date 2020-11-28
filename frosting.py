N = input()
A = map(int, raw_input().split())
B = map(int, raw_input().split())
# white
a1, a2, a3 = 0, 0, 0
b1, b2, b3 = 0, 0, 0
for index, a in enumerate(A):
    if index % 3 == 0:
        a1 += a
    elif index % 3 == 1:
        a2 += a
    else:
        a3 += a
for index, b in enumerate(B):
    if index % 3 == 0:
        b1 += b
    elif index % 3 == 1:
        b2 += b
    else:
        b3 += b
whiteArea = a1 * b1 + a3 * b2 + b3 * a2
yellowArea = a2 * b1 + b2 * a1 + a3 * b3
pinkArea = a3 * b1 + a2 * b2 + a1 * b3
s= '{} {} {}'.format(yellowArea, pinkArea, whiteArea)
print s
