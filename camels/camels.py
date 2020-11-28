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

def countOrdered(ordered, invA, n):
    fw = FenwickTree(n)
    orderedPairs = 0
    for k in ordered:
        index = invA[k]
        count = fw.sum(0, index)
        orderedPairs += count
        fw.inc(index, 1)
    return orderedPairs

N = int(raw_input())
jaap = map(int, raw_input().split())
jan= map(int, raw_input().split())
th = map(int, raw_input().split())
invJaap = {v:k for k, v in enumerate(jaap)}
invJan =  {v:k for k, v in enumerate(jan)}
invTh =  {v:k for k, v in enumerate(th)}

jaapJan = countOrdered(jaap, invJan, N)
janTh = countOrdered(jan, invTh, N)
jaapTh = countOrdered(jaap, invTh, N)
totPairs = N * (N - 1)/2
triplets = ((jaapJan + janTh + jaapTh) - totPairs)/2
print(triplets)
