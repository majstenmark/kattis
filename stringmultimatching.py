import sys
from collections import defaultdict as dd

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

MOD = 10**16 + 61

def hash(s):
    hsh = 0
    L = len(s)
    for i in range(L):
        hsh = (hsh*256 + ord(s[i]))%MOD
    return hsh

def hashes(S, L, currhashes):
    if len(S) < L: return dd(list)

    pw = pow(256, L, MOD)
    hsh = 0
    for i in range(L):
        hsh = (hsh*256 + ord(S[i]))%MOD

    if hsh in currhashes:
        currhashes[hsh].append(0)

    for i in range(L, len(S)):
        hsh = (hsh*256 - ord(S[i-L])*pw + ord(S[i]))%MOD
        if hsh in currhashes:
            currhashes[hsh].append(i - L + 1)
    


def solve(patterns, S):
    lengths = dd(list)
    output_lists = {}
    for p in patterns:
        lengths[len(p)].append(p)

    
    for L, li in lengths.items():
        currhashes = {}
        hashlist = []
        for p in li:
            hsh = hash(p)
            currhashes[hsh] = []
            hashlist.append(hsh)

        hashes(S, L, currhashes)
        for i in range(len(li)):
            p = li[i]
            hsh = hashlist[i]
            output_lists[p] = currhashes[hsh]
        
    out = []
    for p in patterns:
        indeces = ' '.join(map(str, output_lists[p]))
        out.append(indeces)
    return '\n'.join(out)
        

out = []
try:
    while True:
        N = ni()
        
        patterns = [inp() for _ in range(N)]
        S = inp()
       
        res = solve(patterns, S)
        out.append(res)
except:
    print('\n'.join(out))
