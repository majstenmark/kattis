class BitArray(object):
    def __init__(self, lenght):
        self.values = bytearray(b"\x00" * (lenght // 8 + (1 if lenght % 8  else 0)))
        self.lenght = lenght

    def __setitem__(self, index, value):
        value = int(bool(value)) << (7 - index % 8)
        mask = 0xff ^ (1<<(7 - index % 8))
        self.values[index // 8] &= mask
        self.values[index // 8] |= value
    def __getitem__(self, index):
        mask = 1 << (7 - index % 8)
        return bool(self.values[index // 8] & mask)

    def __len__(self):
        return self.lenght

    def __repr__(self):
        return "<{}>".format(", ".join("{:d}".format(value) for value in self))


N, Q = map(int, raw_input().split())
sieve = BitArray(N+1)
queries = [int(raw_input()) for _ in range(Q)]
sieve[0] = 1
sieve[1] = 1

def fill(x):
    for val in range(x * x, N+1, x):
        sieve[val] = 1

for nbr in range(2, N):
    if not sieve[nbr]:
        fill(nbr)

c = 0
for i in range(2, N+1):
    c += (1 - sieve[i])
print(c)

for q in queries:
    print(1 - int(sieve[q]))
