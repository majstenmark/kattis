alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
ind = {ch: i for i, ch in enumerate(alph)}

try:
    while True:
        data = raw_input().split()
        N = int(data[0])
        msg = data[1]
        rev=msg[::-1]
        out = []
        for ch in rev:
            i = ind[ch]
            ni = (i + N) % len(alph)
            out.append(alph[ni])
        print(''.join(out))
except:
    exit()