co = [1, 1, 2, 2, 2, 8]
li = map(int, raw_input().split())
err = [co[i] - li[i] for i in range(6)]
print(' '.join(map(str, err)))