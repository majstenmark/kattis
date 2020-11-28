a1, b1, a2, b2 = map(int, raw_input().split())
a3, b3, a4, b4 = map(int, raw_input().split())
expGunnar = (a1 + b1 + a2 + b2)
expEmma = (a3 + b3 + a4 + b4)
if expGunnar > expEmma:
    print 'Gunnar'
elif expGunnar == expEmma:
    print 'Tie'
else:
    print 'Emma'
