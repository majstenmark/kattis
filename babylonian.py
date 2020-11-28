N = int(raw_input())
for n in range(N):
    line = raw_input().split(',')
    base = 1
    val = 0
    for ch in line[::-1]:
        nbr = 0
        if ch != '':
            nbr = int(ch)
        val += nbr * base
        base *= 60
    print(val)
        
