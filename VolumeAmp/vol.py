N = int(raw_input())

for n in range(N):
    A, Y = map(int, raw_input().split())
    As = map(int, raw_input().split())
    volumes = set([1])
    maximum = 1
    for index in range(len(As)):
        amp = As[index]
        nvols = set()
        for vol in volumes:
            val = vol * amp
            if val <= Y:
                nvols.add(val)
                maximum = max(maximum, val)
        volumes.update(nvols)

    print(maximum)
