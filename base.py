MIN = 1
MAX = pow(2, 32) -1
N = int(input())
bases = '0123456789abcdefghijklmnopqrstuvwxyz0'
digs = {ch: i for i, ch in enumerate(bases)}
digs['0'] = 0
def ones(x):
    return x.count('1') == len(x)

def onebase(x, op, y, z):
    if ones(x) and ones(y) and ones(z):
        xval = len(x)
        yval = len(y)
        zval = len(z)
        if op == '+': return xval + yval == zval
        if op == '-': return xval - yval == zval
        if op == '*': return xval * yval == zval
        if op == '/': return xval == yval * zval
    return False


def maxbase(s):
    ords = map(ord, list(s))
    mx =  max(ords)
    if mx <= ord('9'):
        return int(chr(mx)) +1
    return 11 + (mx - ord('a'))

def tobase(x, base):
    val = 0
    b = 1
    for ch in x[::-1]:
        val += b * digs[ch]
        b *= base
    
    return val

def inrange(x):
    return MIN <= x <= MAX
#a = 10, b = 11, c = 12, d = 13, e = 14, f = 15, g = 16.
def checkbase(x, op, y, z, base):
    xval = tobase(x, base)
    yval = tobase(y, base)
    zval = tobase(z, base)
    #print(xval, yval, zval)
    if inrange(xval) and inrange(yval) and inrange(zval):
        if op == '+': return xval + yval == zval
        if op == '-': return xval - yval == zval
        if op == '*': return xval * yval == zval
        if op == '/': return xval == yval * zval
    return False

for _ in range(N):
    x, op, y, _, z = input().split()
    mxbase = max(maxbase(x), maxbase(y), maxbase(z))
    ok = []
    if onebase(x, op, y, z):
        ok.append('1')
    #print(f"mxbase {mxbase} {bases[mxbase]}")
    for base in range(mxbase, 37):

        if checkbase(x, op, y, z, base):
            ok.append(bases[base])
    if len(ok)> 0:
        print(''.join(ok))
    else:
        print('invalid')