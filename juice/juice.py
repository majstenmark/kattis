from collections import deque
N = int(raw_input())
parents = [[0, 0, 0]]
houses = []
for n in range(1, N + 1):
    p, r, c = map(int, raw_input().split())
    parents.append([p, r, c])
    houses.append((r, n))
q = deque(sorted(houses))
count = 0
def getPower(house):

    p, demand, c = parents[house]
    stack = [house]
    ok = False
    while demand <= c:
        if p == 0:
            ok = True
            break
        stack.append(p)
        p, r, c = parents[p]
    if ok:
        for p in stack:
            parents[p][2] = parents[p][2] - demand
        return True

    return False

while q:
    r, smallest = q.popleft()
    powerUp = getPower(smallest)
    if powerUp:
        #print("Added {}".format(smallest))
        count += 1
print(count)
