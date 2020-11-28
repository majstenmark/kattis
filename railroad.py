X, Y = [int(v) for v in raw_input().split()]
if (Y * 3) % 2 == 0:
    print('possible')
else:
    print('impossible')