orig = raw_input().upper()
c = 0
goal = ['P', 'E', 'R']
for index in range(len(orig)):
    targetLetter = goal[index%3]
    if orig[index] != targetLetter:
        c += 1
print c
