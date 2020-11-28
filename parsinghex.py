import sys
h = '0123456789abcdef'
hex= set(list(h))

curr = []
for line in sys.stdin.readlines():
    inhex = False
    lower = line.lower()
    for i, ch in enumerate(lower):
        if ch == 'x' and i > 0 and lower[i-1] == '0':
            inhex = True
            curr.append('0')
            curr.append(line[i])
        elif inhex and ch in hex:
            curr.append(line[i])
        elif inhex:
            inhex = False
            hex_str = ''.join(curr)
            dec= int(hex_str, 16)
            print('{} {}'.format(hex_str, dec))
            curr = []
