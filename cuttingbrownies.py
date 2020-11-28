inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

mem = {}
def win(b, d):
    if (b, d) in mem:
        return mem[b, d]
    if b == 1:
        mem[b, d] = 0
        return 0
    if d == 1:
        mem[b, d] = 1
        return 1
    h = b //2
    l = win(d, h)
    r = win(d, b - h)
    mem[b, d] = l == r == 0
    return mem[b, d]

T = ni()
for _ in range(T):
    line = inp().split()
    B, D = int(line[0]), int(line[1])
    starter = line[-1]
    if starter == 'Harry':
        w = win(D, B)
    else:
        w = win(B, D)    
    if w:
        print('{} can win'.format(starter))
    else:
        print('{} cannot win'.format(starter))