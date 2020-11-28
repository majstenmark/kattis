N, B = map(int, raw_input().split())
if N > 2 ** (B+1) -1:
    print 'no'
else:
    print 'yes'
