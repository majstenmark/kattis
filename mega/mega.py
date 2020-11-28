
class FenwickTree:
    arr = []
    def __init__(self, n):
        self.arr = [0 for _ in range(n + 1)]

    def inc(self, i, val):
        self.private_inc(i + 1, val)

    def sum(self, a, b):
        return self.private_sum(b+1) - self.private_sum(a)

    def private_inc(self, i, val):

        while i < len(self.arr):
            self.arr[i] += val
            i += i & -i

    def private_sum(self, i):
        s = 0
        while i > 0:
            s += self.arr[i]
            i -= i & -i
        return s


N =int(raw_input())
c = [int(v) for v in raw_input().split()]
cInv = [ [] for _ in range(N)]
for index, value in enumerate(c):
    cInv[value-1].append(index)
values = sorted(c)
megas = 0
nbrs = FenwickTree(N)
inv = FenwickTree(N)
#print(cInv)
dbl = []
for k in range(N):
    for index in cInv[k]:

        thisInv = nbrs.sum(index, N-1)
        megas += inv.sum(index, N-1)
        dbl.append((index, thisInv))
    #print('Adding doubles ', dbl)
    for val, invV in dbl:
        nbrs.inc(val, 1)
        inv.inc(val, invV)
    dbl = []

    #print('When adding {} the nbrs is {} and the inv is {} '.format(k+1, nbrsvals, vals))
#print(inv.sum(0, N -1))

print(megas)
