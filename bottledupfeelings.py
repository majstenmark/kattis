S,V1, V2 = [int(v) for v in raw_input().split()]
max_large = S//V1
for n in range(max_large, -1, -1):
    used_oil = n * V1
    oil_left = S - used_oil
    if oil_left % V2 == 0:
        n2 = oil_left // V2
        #fits the small bottles as well.
        print('{} {}'.format(n, n2))
        exit()
print('Impossible')