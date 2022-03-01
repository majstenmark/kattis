vals = [int(v) for v in input().split()]
towers = vals[0:6]
h = vals[-2:]

def printres(li1, li2):
    t1 = [towers[i] for i in li1]
    t2 = [towers[i] for i in li2]
    t1.sort(reverse = True)
    t2.sort(reverse = True)
    print(f'{t1[0]} {t1[1]} {t1[2]} {t2[0]} {t2[1]} {t2[2]}')
    exit()

for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            index = set([i, j, k])
            h1 = towers[i] + towers[j] + towers[k]
            h2 = 0
            others = []
            for t in range(6):
                if t not in index:
                    others.append(t)
                    h2 += towers[t]
            if h1 == h[0] and h2 == h[1]:
                printres([i, j, k], others)
            if h1 == h[1] and h2 == h[0]:
                printres(others, [i, j,k]) 