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
N = int(raw_input())
orgIndex = [0 for _ in range(N)]
fen = FenwickTree(N)
for n in range(N):
    val = int(raw_input())
    orgIndex[val - 1] = n
    fen.inc(n, 1)

for k in range(N/2):
    orig = orgIndex[k]
    fen.inc(orig, -1)
    swaps = fen.sum(0, orig)
#    print('k = {}, orig = {} and swaps {}'.format(k, orig, swaps))
    print(swaps)

    orig = orgIndex[N - 1- k]
    fen.inc(orig, -1)
    swaps = fen.sum(orig, N - 1)

#    print('k = {}, orig = {} and swaps {}'.format(k, orig, swaps))
    print(swaps)
if N % 2 == 1:
    print(0)
