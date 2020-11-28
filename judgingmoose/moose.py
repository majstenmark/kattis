L, R =map(int, raw_input().split())
if (L < 0 and R < 0) or (L, R) == (0, 0):
    print('Not a moose')
elif L == R:
    print 'Even', 2 * L
else:
    v = 2 * max(L, R)
    print 'Odd', v
