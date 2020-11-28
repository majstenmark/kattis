def tobin(nbr, f, base):
    s = []
    while nbr >0:
        s.append(f[(nbr % base)])
        nbr = nbr //base
    rev = ''.join(s)
    return rev[::-1]

def todec(nbr, d, base):
    dec = 0
    pos = 1
    for digit in nbr[::-1]:
        val = d[digit]
        dec += val * pos
        pos *= base
    return dec


T = int(raw_input())
for t in range(T):
    num, src, target = raw_input().split()
    base1 = len(src)
    d1 = {ch: i for i, ch in enumerate(src)}
    base2 = len(target)
    dec_num = todec(num, d1, base1)
    res = tobin(dec_num, target, base2)
    print('Case #{}: {}'.format(t+1, res))