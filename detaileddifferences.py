N = int(raw_input())
for n in range(N):
    A = raw_input()
    B = raw_input()
    out = []
    for i in range(len(A)):
        if A[i] != B[i]:
            out.append('*')
        else:
            out.append('.')
    print(A)
    print(B)
    print(''.join(out))
    print('\n')