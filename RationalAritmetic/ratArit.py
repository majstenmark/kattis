def gcd(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    return b if a % b == 0 else gcd(b, a % b)


N = int(raw_input())
for n in range(N):
    line = raw_input().split()
    x1, y1, x2, y2 = int(line[0]), int(line[1]), int(line[3]), int(line[4])
    op = line[2]
    rd = y1 * y2
    rx1 = x1 * y2
    rx2 = x2 * y1
    a, b = 0, rd
    if op == '+':
        a = rx1 + rx2
    if op == '-':
        a = rx1 - rx2
    if op == '*':
        a, b = rx1 * rx2, rd * rd
    if op == '/':
        a, b = rx1, rx2

    nd = gcd(a, b)
    top = a / nd
    bott = b /nd
    print('{} / {}'.format(top, bott))
