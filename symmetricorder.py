N = int(raw_input())
cnt = 1
while N > 0:
    pairs = []
    end = N if N%2 ==0 else N-1
    for n in range(0, end, 2):
        name1 = raw_input()
        name2 = raw_input()
        pairs.append((name1, name2))
    if N % 2== 1:
        name1 = raw_input()
        pairs.append((name1, name1))    
    order = [''] * N
    for i, (n1, n2) in enumerate(pairs):
        order[i] = n1
        order[N-1-i] = n2
    print('SET {}'.format(cnt))
    cnt += 1
    res = '\n'.join(order)
    print(res)

    N = int(raw_input())

    