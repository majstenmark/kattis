def testgame(li, ans):
    for guess, resp in li:
        if guess > ans and resp != 'too high':
            return False
        if guess < ans and resp != 'too low':
            return False
        if guess == ans and resp != 'right on':
            return False
    return True

li =[]
while True:
    
    guess = int(raw_input())
    if guess == 0:
        exit()
    ans = raw_input()
    if ans == 'right on':
        if testgame(li, guess):
            print('Stan may be honest')
        else:
            print('Stan is dishonest')
        li = []
    else:
        li.append((guess, ans))