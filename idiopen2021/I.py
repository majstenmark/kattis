from collections import *
try: inp = raw_input
except: inp = input
def ni(): return int(inp())
def nl(): return [int(x) for x in inp().split()]

def rnd(x):
    return x%256

def sub(row, prev):
    out = []
    p = 0
    for i in range(len(row)):
        out.append(rnd(row[i] - p))
        p = row[i]
    return out

def up(row, prev):
    out = []
    for i in range(len(row)):
        out.append(rnd(row[i] - prev[i]))
    return out
    
def avg(row, prev):
    out = []
    p = 0
    for i in range(len(row)):
        out.append(rnd(row[i] - rnd(p + prev[i])//2))
        p = row[i]
    return out

def cnt(b, row):
    return len([r for r in row if r%256 == b%256])

def target(b_i, rows):
    out = []
    last = [0]*X
    C = 0
    for row in rows:
        Ls = [row, sub(row, last), up(row, last), avg(row, last)]
        best = 0
        for nr in Ls:
            best = max(best, cnt(b_i, nr))
        out.append(best)
        C += best
        last = row
    return C

Y, X = nl()
rows = [nl() for _ in range(Y)]

BEST = (0, 0)
for i in range(256):
    BEST = max(BEST, (target(i, rows), i))
print('{} {}'.format(BEST[1], BEST[0]))