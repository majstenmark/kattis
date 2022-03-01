#test length
chars = []
for i in range(26):
    asc = ord('a') + i
    lt = chr(asc)
    chars.append(lt)
    asc_cap = ord('A') + i
    lt_cap = chr(asc_cap)
    chars.append(lt_cap)
for i in range(10):
    chars.append(str(i))

def ask(guess):
    print(guess, flush = True)
    ans = input()
    if 'ACCESS GRANTED' in ans:
        exit()
    ans = ans.replace('ACCESS DENIED (', '')
    ans = ans.replace('ms)', '')
    return int(ans)
    
#test length
slowest = 0, 0
for L in range(1, 21):
    guess = 'A' * L
    time = ask(guess)
    slowest = max(slowest, (time, L))
L = slowest[1]

#test character by chara

def pad(pwd, L):
    s = ''.join(pwd)
    return s + '0' * (L - len(s))

pwd = []

def addone(l):
    slowest = 0, 'A'
    for ch in chars:
        pwd.append(ch)
        time = ask(pad(pwd, L))
        slowest = max(slowest, (time, ch))
        pwd.pop()
    pwd.append(slowest[1])
    

for l in range(L):
    addone(l)
