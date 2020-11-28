def check(L, L2):
    for i in range(len(L)):
        if L[i] != L2[i]:
            return False
    return True


N = int(raw_input())
li = [raw_input() for _ in range(N)]
inc = sorted(li)
dec = sorted(li, reverse = True)
if check(li, inc):
    print('INCREASING')
elif check(li, dec):
    print('DECREASING')
else:
    print('NEITHER')