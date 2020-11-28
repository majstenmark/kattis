import sys
lines = sys.stdin.readlines()
for linestr in lines:
    line = linestr.split()
    N = int(line[0])
    Ms = [int(x) for x in line[2:]]
    states = [0] * (N + 1)
    for i in range(N):
        if states[i] == 0:
            for m in Ms:
                if i + m <= N:
                    states[i + m] = 1
    if states[N] == 1:
        print('Stan wins')
    else:
        print('Ollie wins')