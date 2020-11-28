
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
curr = [int(v) for v in raw_input().split()]
cInv = [0] * N
dInv = [0] * N
desired = [int(v) for v in raw_input().split()]
for index, value in enumerate(curr):
    cInv[value-1] = index
for index, value in enumerate(desired):
    dInv[value-1] = index


def countInversions(invA):
    fw = FenwickTree(N)
    inversions = 0
    for k in range(N):
        index = invA[k]
        count = fw.sum(index, N-1)
        inversions += count
        fw.inc(index, 1)
    return inversions

invCurr = countInversions(cInv)
invDes = countInversions(dInv)
if invCurr % 2 == invDes % 2:
    print('Possible')
else:
    print('Impossible')
