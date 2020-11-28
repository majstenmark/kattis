N = int(raw_input())
for n in range(N):
    K = int(raw_input())
    name = raw_input()
    menu = [raw_input() for _ in range(K)]
    ps, pc = False, False
    for item in menu:
        if item == 'pea soup':
            ps =True
        if item == 'pancakes':
            pc = True
    if ps and pc:
        print(name)
        exit()
print('Anywhere is fine I guess')