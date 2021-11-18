N = int(input())
times = []
values = []
area = 0
for n in range(N):
    t, v = input().split()
    t = int(t)
    v = float(v)
    times.append(t)
    values.append(v)
for i in range(1, N):
    dt = times[i] - times[i-1]
    dv = (values[i] + values[i-1])/2
    area += dt * dv
area = area /1000
print(area)

    