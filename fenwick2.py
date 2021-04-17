
def inc(arr, i, val):
    private_inc(arr, i + 1, val)

def fen_sum(arr, a):
    return private_sum(arr, a)

def private_inc(arr, i, val):
    while i < len(arr):
        arr[i] += val
        i += i & -i

def private_sum(arr, i):
    s = 0
    while i > 0:
        s += arr[i]
        i -= i & -i
    return s
'''
class BR:
    def __init__(self):
        self.start = 0
        self.cache = ''
        self.readsize = 2**18
    def readline(self):
        s = self.start
        found = False
        while self.start < len(self.cache):
            if self.cache[self.start] == '\n':
                found = True
                break
            self.start += 1
        s = self.cache[s:self.start]
        if not found:
            self.start = 0
            self.cache = sys.stdin.read(self.readsize)
            while self.start < len(self.cache):
                if self.cache[self.start] == '\n':
                    found = True
                    break
                self.start += 1
            s += self.cache[:self.start]
        self.start += 1
        return s

'''

import sys

#data = sys.stdin.read().split('\n')
CURR_IDX = -1
#br = BR()
def inp():
    return next(sys.stdin)
    global CURR_IDX
    CURR_IDX += 1
    return data[CURR_IDX]

N, Q  = map(int, inp().split())

arr = [0] * (N + 1)
out = []
SZ = 2048
tot = 0
for q in range(Q):
    query = inp().split()
    x = int(query[1])
    if query[0] == '+':
        y = int(query[2])
        inc(arr, x, y)
    else:
        s = str(fen_sum(arr, x))
        tot += len(s) + 1
        out.append(s)
        if tot >= SZ-1:
            tot = 0
            v = '\n'.join(out)
            output = v[:SZ]
            sys.stdout.write(output)
            out = [v[SZ:]]
sys.stdout.write('\n'.join(out))