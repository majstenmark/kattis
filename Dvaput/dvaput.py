P = 1181118711931201
x = 26

def my_hash(p, L):
    pHash = 0
    for k in range(L):
        pHash *= x
        pHash += ord(p[k])
        pHash %= P
    return pHash

def match(text, L):
    X = pow(x, (L -1), P)

    ha = my_hash(text, L)
    matches = set([ha])

    for first in range(len(text) - L):
        ha -= (ord(text[first]) * X)
        ha *= x
        ha += ord(text[first + L])
        ha %= P
        if ha in matches:
            return True
        matches.add(ha)

    return False

def binSearch(text):
    minK = 0
    maxK = len(text)-1
    while minK < maxK:
        midK = (minK + maxK +1)/2
        if match(text, midK):
            minK = midK
        else:
            maxK = midK -1
    return maxK

L = int(raw_input())
text = raw_input()
print(binSearch(text))
