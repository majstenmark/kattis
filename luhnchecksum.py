T = int(raw_input())
for t in range(T):
    nbr = raw_input()
    val = 0
    for i, ds in enumerate(nbr[::-1]):
        d = int(ds)
        if i %2 == 1:
            n = 2 * d
            ent = n % 10
            dec = (n //10) % 10
            val += (ent + dec)
        else:
            val += d
    if val % 10 == 0:
        print('PASS')
    else:
        print('FAIL') 