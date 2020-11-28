limit, n_events = map(int, input().split())
def read():
    line = input().split()
    return (line[0], int(line[1]))

events = [read() for i in range(n_events)]
ppl = 0
reject = 0
for event in events:
    if event[0] == 'leave':
        ppl -= event[1]
    if event[0] == 'enter':
        if ppl + event[1] <= limit:
            ppl += event[1]
        else:
            reject += 1
print(reject)
