import sys
P = 10 ** 9 + 4123
x = 256

def my_hash(p):
    pHash = 0
    for k in range(len(p)):
        pHash *= x
        pHash += ord(p[k])
        pHash %= P
    return pHash

def match(p, t):
    X = pow(x, (len(p) -1), P)
    if len(p) > len(t):
        return []
    pHash = my_hash(p)
    wHash = my_hash(t[0:len(p)])
    matches = []

    if wHash == pHash:
        matches.append(0)
    for first in range(len(t) - len(p)):
        wHash -= (ord(t[first]) * X)
        wHash *= x
        wHash += ord(t[first + len(p)])
        wHash %= P
        if wHash == pHash:
            matches.append(first + 1)
    return matches

data = sys.stdin.read().strip().split('\n')
pairs = [(data[i], data[i+1]) for i in range(0, len(data), 2)]
for pattern, text in pairs:
    #print pattern, text
    matchings = match(pattern, text)
    print ' '.join(map(str, matchings))
