inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

err_msg = 'measurement error'
N = ni()

mins = 0
secs = 0
for _ in range(N):
    M, S = nl()
    mins += M
    secs += S

av = secs/(60 * mins)
if av <= 1:
    print(err_msg)
else:
    print(av)
