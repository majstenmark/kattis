from heapq import heappush as push, heappop as pop

def nl():
    return [int(v) for v in raw_input().split()]

def ni():
    return int(raw_input())
N, K = nl()
persons = [nl() for _ in range(N)]
persons.sort()
m = 0
pq = []
for a, b in persons:
    while pq:
        v = pop(pq)
        if v + K >= a:
            push(pq, v)
            break
    push(pq, b)
    m = max(m, len(pq))
print(m)