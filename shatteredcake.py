W = input()
N = input()
area = 0
for n in range(N):
    w, l = map(int, raw_input().split())
    area += w * l
L = area/W
print L
