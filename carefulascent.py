x,y = [int(v) for v in raw_input().split()]
N = int(raw_input())
H = 0.0
F = 0.0
for n in range(N):
    line = raw_input().split()
    lo= int(line[0])
    hi = int(line[1])
    f =float(line[2])
    h = hi - lo
    H += h
    F += f * h
hvel = x/(y - H + F)
print(hvel)
