from heapq import heappop, heappush

N, T = map(int, raw_input().split())
ppl = []
for n in range(N):
    ci, ti = map(int, raw_input().split())
    ppl.append((ti,ci))
ppl.sort()
q = []
for ti, ci in ppl:
    if ti >= len(q):
         heappush(q, ci)
    else:
        poorest = q[0]
        if ci > poorest:
            heappop(q)
            heappush(q,ci)
#print q
print sum(q)
