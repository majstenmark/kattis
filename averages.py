import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

T = ni()

for _ in range(T):
    inp()
    Ncs, Ne = nl()
    cs = nl()
    e = nl()
    esum = sum(e)
    e_startav = esum/Ne
    cssum = sum(cs)
    cs_startav = cssum/Ncs
    cnt = 0
    for iq in cs:
        cs_new = cssum - iq
        cs_newav = cs_new/(Ncs-1)
        e_new = esum + iq
        e_newav = e_new/(Ne + 1)
        if cs_newav > cs_startav and e_newav > e_startav:
            cnt += 1
    print(cnt) 
