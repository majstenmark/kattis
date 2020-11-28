N = int(raw_input())
runners = []
for n in range(N):
    data = raw_input().split()
    name = data[0]
    leg1 = float(data[1])
    legX = float(data[2])
    runners.append((name, leg1,legX))

sortedBy1= sorted(runners, key=lambda x: x[1])
sortedByX = sorted(runners, key=lambda x: x[2])
# only need to check 4
fastest = 10 **12
team = []

for index in range(4):
    name, time1, timeX = sortedBy1[index]
    time = time1
    others = []
    i = 0
    while len(others) < 3:
        n, t1, t2 = sortedByX[i]

        if n !=name:

            others.append(n)
            time += t2
        i += 1
    if time < fastest:
        fastest = time
        team = [name] + others
print(fastest)
for runner in team:
    print(runner)
