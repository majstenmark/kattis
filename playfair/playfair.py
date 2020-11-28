

def rule2(u):

    a, b  = u
    r, c = mapping[a]
    ra = table[r][(c + 1)%5]
    rr, cc = mapping[b]
    rb = table[rr][(cc + 1)%5]
    return ra, rb


def rule3(u):
    a, b  = u
    r, c = mapping[a]
    ra = table[(r + 1)%5][c]
    rr, cc = mapping[b]
    rb = table[(rr + 1)%5][cc]
    return ra, rb


def rule4(u):

    a, b  = u

    r, c = mapping[a]
    rr, cc = mapping[b]
    ra = table[r][cc]
    rb = table[rr][c]
    return ra, rb



AB = 'abcdefghijklmnoprstuvwxyz'
KEY = raw_input().lower().replace(' ', '') + AB
plaintext = raw_input().lower().replace(' ', '')
mapping= {}
table = [['x'] * 5 for _ in range(5)]
used = set()
ch = 0
for r in range(5):
    for c in range(5):
        while KEY[ch] in used:
            ch+= 1
        mapping[KEY[ch]] = (r,c)
        table[r][c] = KEY[ch]
        used.add(KEY[ch])

pairs = []
index = 0
while index < len(plaintext)-1:
    a  = plaintext[index]
    b = plaintext[index +1]
    if a == b:
        pairs.append((a, 'x'))
        index += 1
    else:
        pairs.append((a, b))
        index += 2
if index < len(plaintext):
    pairs.append((plaintext[-1], 'x'))


out = []
for pair in pairs:

    r1, c1 = mapping[pair[0]]
    r2, c2 = mapping[pair[1]]
    res = pair
    if r1 == r2:
        res = rule2(pair)
    elif c1 == c2:
        res = rule3(pair)
    else:
        res = rule4(pair)
    out.extend([res[0], res[1]])
#print out
print ''.join(out).upper()
