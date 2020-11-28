from collections import defaultdict as dd

T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    words1 = dd(list)
    words2 = dd(list)
    for n in range(N):
        name = raw_input()
        lang1 = raw_input().split()
        lang2 =raw_input().split()
        for w1 in lang1[1:]:
            words1[w1].append(str(n))
        for w2 in lang2[1:]:
            words2[w2].append(str(n))
    pizzas = {}
    for k, v in words1.items():
        s= ''.join(v)
        if s not in pizzas:
            pizzas[s] = [[],[]]
        pizzas[s][0].append(k)
    for k, v in words2.items():
        s= ''.join(v)
        if s not in pizzas:
            pizzas[s] = [[],[]]
        pizzas[s][1].append(k)
    pairs = []
    for k in pizzas.keys():
        l1, l2 = pizzas[k]
        for w1 in l1:
            for w2 in l2:
                pairs.append((w1,w2))
    pairs.sort()
    for p in pairs:
        print('({}, {})'.format(p[0], p[1]))
    print('')