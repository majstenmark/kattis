def dist2(xx, x, yy, y, r2):
    return ((xx - x) ** 2 + (yy - y) ** 2) <= r2

def sprinkle(x, y, r):
    startX = max(0, x - r -1)
    endX = min(10000, x+ r + 1)
    startY = max(0, y - r-1)
    endY = min(10000, y + r + 1)
    r2 = r**2
    for xx in range(startX, endX):
        for yy in range(startY, endY):
            garden[xx][yy] = garden[xx][yy] or dist2(xx, x, yy, y, r2)


G = input()
goblins = []
for g in range(G):
    x, y = map(int, raw_input().split())
    goblins.append((x, y))
M =input()

garden = [[False] * 10001 for _ in range(10001)]

for m in range(M):
    x, y, r = map(int, raw_input().split())
    sprinkle(x, y, r)

c = 0
for x in range(10001):
    for y in range(10001):
        if garden[x][y]:
            c += 1
print c

count = 0
for x, y in goblins:
    if not garden[x][y]:
        count += 1
print count
