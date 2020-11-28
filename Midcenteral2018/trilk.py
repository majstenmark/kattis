moves = raw_input()



pos = [1, 0, 0]
for move in moves:
    if move == 'A':
        pos[0],pos[1] = pos[1], pos[0]

    if move == 'B':
        pos[1],pos[2] = pos[2], pos[1]

    if move == 'C':
        pos[0],pos[2] = pos[2], pos[0]
for n in range(3):
    if pos[n] == 1:
        print n+1
