def tooFew(N, K):
    k = bin(N).count('1')
    arr = ['0'] * (64 - len(bin(N)[2:])) + [c for c in bin(N)[2:]]
    for i in range(len(arr) -1, 0, -1):
        if arr[i] == '0':
            arr[i] = '1'
            k += 1
            if k == K:
                break

    return int(''.join(arr), 2)

def tooMany(N, K):
    smallest2pot = N & (-N)
    tmp = N
    k = bin(tmp).count('1')
    #print('smallest ', smallest2pot)
    #print(k)
    while k > K:

        smallest2pot = tmp & (-tmp)
        tmp += smallest2pot
        k = bin(tmp).count('1')
        if k < K:
            return tooFew(tmp, K)

    return tmp


def exactly(N):
    arr = ['0'] * (64 - len(bin(N)[2:])) + [c for c in bin(N)[2:]]
    expand = True
    for i in range(len(arr) -1, len(arr) - len(bin(N)[2:]), -1):
        if arr[i] == '1' and arr[i - 1] == '0':
            arr[i] = '0'
            arr[i - 1] = '1'
            expand = False
    if expand:
        arr = ['0'] * 64
        arr[len(arr) - len(bin(N)[2:]) -1] = '1'
        for i in range(len(arr) -1, len(arr) - K, -1):
            arr[i] = '1'


    return int(''.join(arr), 2)



N, K = map(int, raw_input().split())
k = bin(N).count('1')
if k < K:
    print(tooFew(N, K))
if k == K:
    print(exactly(N))
if k > K:
    print(tooMany(N, K))
