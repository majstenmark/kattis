N = int(raw_input())
for n in range(N):
    r, e, c = [int(v) for v in raw_input().split()]
    if r < e - c:
        print('advertise')
    elif r == e -c:
        print('does not matter')
    else:
        print('do not advertise') 