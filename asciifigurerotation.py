import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def pad(orig):
    mx = 0
    for r in orig:
        mx = max(mx, len(r))
    padded = []
    for r in orig:
        p = r + ' ' * (mx - len(r))
        padded.append(p)
    return padded

def swap(rot):
    swapped = []
    for row in rot:
        new_row = []
        for ch in row:
            if ch == '-':
                new_row.append('|')
            elif ch == '|':
                new_row.append('-')
            else:
                new_row.append(ch)
        swapped.append(new_row)
    return swapped

def rotate(orig):
    padded = pad(orig)
    no_rows = len(padded[0])
    rot = []
    for row in range(no_rows):
        new_row = []
        for r in padded[::-1]:
            #print(r, row, no_rows)
            new_row.append(r[row])
        rot.append(new_row)
    return swap(rot)


N = ni()
while True:
    
    orig = [inp() for _ in range(N)]
    rot = rotate(orig)
    out = []
    for row in rot:
        s = ''.join(row).rstrip()
        out.append(s)
    print('\n'.join(out))
    N = ni()
    if N == 0: exit()
    print('')
    