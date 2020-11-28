N = int(raw_input())
ps = [int(v) for v in raw_input().split()]
tape = 0.0
dims = (2 ** (-3.0/4), 2 ** (-5.0/4))
needed = 2
for n in range(len(ps)):
    cnt = ps[n]
    tape += dims[0]* (needed/2)
    needed -= cnt
    if needed <= 0:
        print(tape)
        exit()
    dims = dims[1], dims[0]/2.0
    needed *= 2
print('impossible')