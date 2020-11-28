L = int(raw_input())
D = int(raw_input())
X = int(raw_input())

def check(nbr, X):
    s = 0
    while nbr > 0:
        s += nbr % 10
        nbr = nbr //10
    return s == X


for n in range(L, D +1):
    if check(n, X):
        break

for m in range(D,L -1, -1):
    if check(m, X):
        break
print(n)
print(m)
