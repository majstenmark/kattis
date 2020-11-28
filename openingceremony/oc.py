from collections import deque
N=int(raw_input())
hs=[int(v) for v in raw_input().split()]
h_shots=0
hs.sort(key=lambda x: -x)
total=0
q = deque(hs)
while q and h_shots < q[0]:
    if q[0] - h_shots > len(q):
        q.popleft()
        total +=1
    else:
        h_shots+=1
        total+=1
        while q and q[-1]-h_shots<=0:
            q.pop()
print(total)
