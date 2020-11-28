
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

T =int(raw_input())
for t in range(T):
    M, R =map(int, raw_input().split())
    queries = [int(v) for v in raw_input().split()]
    N = M + R
    movieIndex = [R + i for i in range(N)]
    fw = FenwickTree(N)
    for movie in movieIndex:
        fw.inc(movie, 1)
    answers = []
    for r in range(R):
        q = queries[r]
        index = movieIndex[q-1]
        fw.inc(index, -1)
        ans = fw.sum(0, index - 1)
        movieIndex[q-1] = R - r - 1
        fw.inc(R - r - 1, 1)
        answers.append(str(ans))
    print(' '.join(answers))
