def solve(N):
    if N  == 1:
        print('{ }')
    else:
        b = bin(N-1)[2:]
        s = []
        for i, bit in enumerate(b[::-1]):
            if bit == '1':
                s.append(3 ** i)
        s_str = '{ ' + ', '.join(map(str, s)) + ' }'
        print(s_str)
N = int(raw_input())
while N > 0:
    solve(N)
    N = int(raw_input())