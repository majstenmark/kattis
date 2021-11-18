import random
curr = 0
guess = 1

print(guess, flush = True)
while curr != 99:
    curr = int(input())
    if curr % 3 == 0:
        rand = random.randint(1, 2)
        print(curr+rand, flush = True)
    else:
        if (curr + 1) % 3 == 0:
            print(curr+1, flush = True)
            if curr+1 == 99: exit()
        else:
            print(curr+2, flush = True)
            if curr+2 == 99: exit()
        
