inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
for n in range(N):
    d = ni()
    left = []
    right = []
    power = 1
    while d:
        r = d % 3
        if r == 1:
            right.append(power)
        elif r == 2:
            left.append(power)
            d += 1
        d //= 3
        power *= 3
    L = ' '.join(map(str, left[::-1]))
    R = ' '.join(map(str, right[::-1]))
    print('left pan: {}'.format(L))
    print('right pan: {}'.format(R))
    print('')