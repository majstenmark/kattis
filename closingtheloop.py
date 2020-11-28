N = int(raw_input())

for n in range(N):
    red =[]
    blue =[]
    R = int(raw_input())
    line = raw_input().split()
    for rope in line:
        L = int(rope[:-1])
        col = rope[-1]
        if col =='R':
            red.append(L)
        else:
            blue.append(L)
    mx = min(len(red), len(blue))
    red.sort(reverse= True)
    blue.sort(reverse= True)
    loop = 0
    if mx == 0:
        print('Case #{}: {}'.format(n+1, 0))
    else:
        for i in range(mx):
            loop += red[i]
            loop += blue[i]
        loop -= 2* mx
        print('Case #{}: {}'.format(n+1, loop))