import sys
from collections import defaultdict as dd

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())
def nx(): 
    data = inp().split()
    out = []
    for c in data:
        if c in 'TLSD':
            out.append(c)
        else:
            out.append(int(c))
    return out

def two_color(g, first):
    color = dd(int)
    q = [first]
    color[first] = 1
    while q:
        q2 = []
        for p in q:
            if 

def consistent(li):
    s1 = set()
    s2 = set()
    g = dd(list)
    first = -1
    for t, j, k in li:
        if t == 'D':
            g[j].append(k)
            g[k].append(j)
            first = max([first, j, k])
    return two_color(g, first)
                

def find_liars(N, ppl_stms, stms_about_person):
    start = ['-'] * N
    found = []
    for i in range(N):
        if not consistent(ppl_stms[i]):
            found.append(i)
            start[i] = 'L'
    for f in found:
        ok, start = propagate(start, f, ppl_stms, stms_about_person)
    return start



def solve(N, M, statements):
    ppl_stms = dd(list)
    stms_about_person = dd(list)
    for stm in statements:
        i = stm[0]
        t = stm[1]
        j = stm[2]
        k = 0 if len(stm) == 3 else stm[3]
        ppl_stms[i].append((t, j, k))
        stms_about_person[j].append((i, t, k))
    start = find_liars(N, ppl_stms)
    for i in range(N):
        if start[i] == '-':
            #test both.
            start[i] = 'T'
            ok, alt = propagate(start, i, ppl_stms, stms_about_person)
            start[i] = 'L'
            ok2, alt2 = propagate(start, i, ppl_stms, stms_about_person)
            if ok and ok2:
                start = merge(alt, alt2)
                start[i] = '-'
            elif ok:
                start = merge(start, alt)
                start[i] = 'T'
            elif ok2:
                start = merge(start, alt2)
                start[i] = 'L'
        
    return ' '.join(start)
    
T = int(inp())
for t in range(T):
    N, M = nl()
    statements = [nx() for _ in range(M)]
    R = solve(N, M, statemetns)

    print('Case #{}: {}'.format(t+1, R))