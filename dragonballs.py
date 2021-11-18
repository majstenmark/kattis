def dist2(x, y, X, Y):
    return (x - X)**2 + (y - Y)**2

def getpos(X, Y, d2):
    d = int(d2 ** 0.5) + 1
    possible = set()
    y = d
    #print('Setting y ', d)
    x = 0
    while y >= 0:
        while dist2(X, Y, x, y) < d2:
            x += 1
        if dist2(X, Y, x, y) == d2:
            possible.add((x, y))
        y -= 1
    return possible

def ask(alts):
    for x, y in alts:
        print(f'{x} {y}', flush = True)
        ans = int(input())
        if ans == 0:
            return 1
    return 0

def ok(x, y, possible, d2):
    pos = set()
    for xx, yy in possible:
        if dist2(x, y, xx, yy) == d2:
            pos.add((xx, yy))
    return pos

def find():
    print('0 0', flush = True)
    d1_2 = int(input())
    if d1_2 == 0: return 1
    print('1 0', flush = True)
    d2_2 = int(input())

    if d2_2 == 0: return 1
    print('0 1', flush = True)
    d3_2 = int(input())
    if d3_2 == 0: return 1
    pos1 = getpos(0, 0, d1_2)
    pos2 = ok(1, 0, pos1, d2_2)
    pos3 = ok(0, 1, pos1, d3_2)
    #print(pos1)
    #print(pos2)
    #print(pos3)
    found = ask(pos2)
    if found > 0: return found
    found = ask(pos3)
    return found
    
    
    

N = int(input())
n = 0
while n < N:
    n += find()
exit()
    