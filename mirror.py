inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

T = ni()
for t in range(T):
    R, C = nl()
    grid =[inp() for _ in range(R)]
    print('Test {}'.format(t+1))
    for r in range(R-1, -1, -1):
        s = grid[r]
        print(s[::-1])