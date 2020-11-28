inp = raw_input

def nl():
    return [int(v) for v in inp().split()]

def solve(S):
    return ''
    
P, T = nl()
cnt = 0
for t in range(P):
    ok = True
    for p in range(T):
        s = inp()
        a = s[0].lower() + s[1:]
        all_low = s.lower()
        if a != all_low:
            ok = False
    if ok:
        cnt += 1
print(cnt)