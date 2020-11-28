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


N = input()
a = []
b= []
fen = FenwickTree(N)

for n in range(N):
    nbr = input()
    a.append(nbr)
    b.append(nbr)
a.sort()
remap = {}
for index, val in enumerate(a):
    remap[val] = index

cnt = 0
for d in b:
    index= remap[d]
    cnt += fen.sum(index,N-1)
    fen.inc(index,1)
print cnt
