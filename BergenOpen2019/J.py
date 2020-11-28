def nl():
    return [int(v) for v in raw_input().split()]

def ni():
    return int(raw_input())

from heapq import heappush as push, heappop as pop
N, M , K = nl()
pq = []
for n in range(N):
    _, book, s = raw_input().split('"')
    page = int(s)
    push(pq, (book, page))
li = []
for n in range(M):
    t, book, s = raw_input().split('"')
    ti, si = int(t),int(s)
    li.append((ti, book, si))
li.sort(reverse = True)
JE = "Jane Eyre"
push(pq, (JE, K))
time = 0
while True:
    while li:
        if li[-1][0] <= time:
            ti, book, si = li.pop()
            push(pq, (book, si))
        else:
            break
    book, si = pop(pq)
    time += si
    if book == JE:
        print(time)
        exit()