def inside(x, y, x1, y1, x2, y2):
    return x1 <= x <= x2 and y1 <= y <= y2

def gcd(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    return b if a % b == 0 else gcd(b, a % b)

Xb, Yb = map(int, raw_input().split())
X1, Y1, X2, Y2 = map(int, raw_input().split())
g = gcd(Xb,Yb)
Tx = Xb/g
Ty = Yb/g
if inside(Tx, Ty, X1, Y1, X2, Y2):
    if inside(Xb, Yb, X1, Y1, X2, Y2):
        print 'Yes'
    else:
        k = min((X2 + Tx -1)/Tx, (Y2 + Ty -1)/Ty)
        nTx = k * Tx
        nTy = k * Ty
        while inside(nTx, nTy, X1, Y1, X2, Y2):
            k += 1
            nTx = k * Tx
            nTy = k * Ty

        if (nTx, nTy) == (Xb,Yb):
            print 'Yes'
        else:
            print 'No'
            print '{} {}'.format(nTx, nTy)

else:

    if (Tx, Ty) == (Xb,Yb):
        print 'Yes'
    else:
        print 'No'
        print '{} {}'.format(Tx, Ty)
