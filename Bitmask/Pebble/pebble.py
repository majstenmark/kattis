def gen(i):
    ne = []
    for j in range(10):
        if (i & 1 << j) == 0 and (i & 1<<(j+1)) != 0 and (i & 1 << (j + 2)) != 0:
            mask = 7 << j
            r = mask ^ i
            ne.append(r)
        if (i & 1 << j) != 0 and (i & 1<<(j+1)) != 0 and (i & 1 << (j + 2)) == 0:
            mask = 7 << j
            r = mask ^ i
            ne.append(r)

    return ne

def test():
    t = '1100' #
    ne = gen(int(t, 2))
    for n in ne:
        print(bin(n)[2:])

def bfs(q):
    while q:
        q2 = []
        for node in q:
            for ne in gen(node):
                if not visited[ne]:
                    visited[ne] = True
                    q2.append(ne)
        q = q2
    return bin(node).count('1')

#test()
#exit()

N  = int(raw_input())
for test in range(N):
    visited = [False for _ in range(2**12)]
    board = raw_input()
    bits = []
    for ch in board:
        bi = '1' if ch == 'o' else '0'
        bits.append(bi)
    i = int(''.join(bits), 2)
    visited[i] = True
    pebbles = bfs([i])
    print(pebbles)
