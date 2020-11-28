N = int(raw_input())
for n in range(N):
    data  = raw_input().split()
    f = data[0]
    D = int(data[1])
    H = int(data[2])
    M = int(data[3])
    totMin = (H+24) * 60 + M
    newMin = totMin - D
    if f == 'F':
        newMin = totMin + D
    nH = (newMin // 60) % 24
    nM = newMin % 60
    print('{} {}'.format(nH, nM))