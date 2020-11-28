n, p,k = map(int, raw_input().split())
ti = [0] + map(int, raw_input().split()) + [k]
si = [ti[i+1] - ti[i] for i in range(len(ti) -1)]
time = 0
for i, seg in enumerate(si):
    time += seg* (100 + i * p)/100.0
print(time)