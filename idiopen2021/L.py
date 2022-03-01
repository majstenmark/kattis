from collections import *
try: inp = raw_input
except: inp = input
def ni(): return int(inp())
def nl(): return [int(x) for x in inp().split()]

N, M = nl()
a, b, c, d, e, f, v0 = nl()

def nextV(i, oldV):
    return (a*i + b*oldV)%c + 1
def nextL(i, oldV):
    return (d*i + e*oldV)%f


states = {(0, v0) : 0} # (filled, last, score)
for i in range(M):
    states_new = Counter()
    for (filled, last), score in states.items():
        p_sz = nextV(i+1, last)
        p_sc = nextL(i+1, last)
        states_new[filled, p_sz] = max(states_new[filled, p_sz], score)
        new_f = p_sz + filled
        if new_f <= N:
            states_new[new_f, 0] = max(states_new[new_f, 0], score + p_sc)
    states = states_new
print(max(states.values()))



