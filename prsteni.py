inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def gcd(a, b):return gcd(b, a % b) if b else a

N = ni()
r = nl()
first = r[0]
for other in r[1:]:
    v = gcd(other, first)
    print('{}/{}'.format(first//v, other//v))

