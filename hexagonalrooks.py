from collections import defaultdict as dd
A, B = input().split()

grid = set()
rows = 6
for col in range(-5, 6):
    for r in range(rows):
        grid.add((col, r))
    if col < 0:
        rows += 1
    else:
        rows -= 1
g = dd(list)
for c, r in grid:
    if c < 0:
        alt = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
    elif c == 0:
        alt = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]
    else:
        alt = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
    for dc, dr in alt:
        cc = c + dc
        rr = r + dr
        if (cc, rr) in grid:
            g[c, r].append((cc, rr))
        else:
            g[c, r].append(None)

def move(c, r, dir):
    if g[c, r][dir] != None:
        cc, rr = g[c, r][dir]
        for step in range(1, 12):
            if (cc, rr) in grid:
                G[c, r].append((cc, rr))
            if g[cc, rr][dir] == None: return
            cc, rr = g[cc, rr][dir]

G = dd(list)
for c, r in g.keys():
    for dir in range(6):
        move(c, r, dir)


alph = {'a': -5, 'b': -4, 'c': -3, 'd': -2, 'e': -1, 'f': 0, 'g': 1, 'h': 2, 'i': 3, 'j': 4, 'k': 5}
start = alph[A[0]], int(A[1:]) -1
end = alph[B[0]], int(B[1:]) -1
cnt = 0
for move1 in G[start]:
    for move2 in G[move1]:
        if move2 == end:
            cnt += 1
print(cnt)