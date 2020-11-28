from math import sqrt as sq

def dist(me, them):
    return sq((me[0] - them[0])**2 + (me[1] - them[1])**2)

X, Y, N = map(int, raw_input().split())
sensors = []
for n in range(N):
    sx, sy, sr = map(int, raw_input().split())
    d = dist((X, Y), (sx, sy))
    sensors.append((d - sr, sx, sy, sr))
sensors.sort()
if sensors[2][0] <= 0:
    print(0)
else:
    print(int(sensors[2][0]))