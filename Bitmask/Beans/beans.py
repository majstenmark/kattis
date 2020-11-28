B = int(raw_input())
Vs = map(int, raw_input().split())
T = int(raw_input())

def price(sub):
    cow = 0
    for j in range(B):
        if 1 <<j & sub == 0:
            cow += Vs[j]
    return cow

def check(sub):
    inAll = True
    for farm in farms:
        inAll = inAll & (sub & farm != 0)
        if not inAll:
            return False
    return True
farms = []
for i in range(T):
    bi = sum(map(lambda x: 2 ** (int(x)-1), raw_input().split()[1:]))
    farms.append(bi)
cows = 0
for sub in range(2 ** B):
    if check(sub):
        cows = max(cows, price(sub))
print(cows)
