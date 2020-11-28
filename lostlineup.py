N = int(raw_input())
diff = [int(v) for v in raw_input().split()]
line = [0] * N
line[0] = str(1)
for i, d in enumerate(diff):
    name = i + 2
    index = 1 + d
    line[index] = str(name)
out= ' '.join(line)
print(out)
