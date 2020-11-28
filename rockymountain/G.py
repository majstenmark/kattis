N = int(raw_input())
qaly = 0.0
for n in range(N):
    Q, L = map(float, raw_input().split())
    qaly+= Q * L
print qaly
