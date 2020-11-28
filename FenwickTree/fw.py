class FenwickTree:
    arr = []
    def __init__(self, n):
        self.arr = [0 for _ in range(n + 1)]

    def inc(self, i, val):
        self.private_inc(i + 1, val)

    def sum(self, a):
        return self.private_sum(a)

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

N, Q  = map(int, raw_input().split())
fen = FenwickTree(N)
for q in range(Q):
    query = raw_input().split()
    x = int(query[1])
    if query[0] == '+':
        y = int(query[2])
        fen.inc(x, y)
    else:
        print(fen.sum(x))
