N= int(raw_input())
pw = [float(raw_input().split()[1]) for n in range(N)]
pw.sort(reverse = True)
rounds= 0.0
for n in range(N):
    rounds += (n+1) * pw[n]
print(rounds)