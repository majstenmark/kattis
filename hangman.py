W = raw_input()
guess = raw_input()
left = set(W)
wrong = set()
for letter in guess:
    if letter in left:
        left.remove(letter)
        if len(left) == 0:
            print('WIN')
            exit()
    else:
        wrong.add(letter)
        if len(wrong) == 10:
            print('LOSE')
            exit()
         