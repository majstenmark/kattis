def neig(sq):
    good = []

    cand = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (-1, 1), (0, -1),(-1, -1)]
    for c in cand:
        x, y= sq[0] + c[0], sq[1] + c[1]
        if 0 <= x< N and 0 <= y < N:
            good.append((x, y))
    return good

def findmov3
6 2 2
1 2
8 3 3
1 4 7
6 4 4
1 2 5 6es(q, myzergs,z):
    INF = 10**12
    visited = [[INF] * N for _ in range(N)]
    for node in q:
        visited[node[0]][node[1]] = 0
    while q:
        q2 = []
        for node in q:
            for sq in neig(node):
                if visited[sq[0]][sq[1]] == INF:
                    visited[sq[0]][sq[1]] = visited[node[0]][node[1]] + 1
                    q2.append(sq)
        q = q2
    moves = []
    for sq in myzergs:
        cand = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (-1, 1), (0, -1),(-1, -1)]
        for c in cand:
            x, y= sq[0] + c[0], sq[1] + c[1]
            if 0 <= x< N and 0 <= y < N:
                if visited[x][y] < visited[sq[0]][sq[1]]:
                    moves.append((sq, (x, y)))
                    continue
    return moves    

def do(dec, stays, board):
    for t, sq in dec:
        if t == 'a':
            

def decide(z, enemy):
    dec = {}
    stays = {}
    move = []
    for _, row, col in z:
        attack, sq = checkattack(row, col, enemy)
        if attack:
            dec[sq] = 'a', (row, col)
            stays.add((row, col))
        else:
            move.append((row, col))
    moves = findmoves(enemy, move, z)
    for fr, to in moves:
        if to in dec:
            _, other = dec[to]
            if fr[0] < other[0] or (fr[0] == other[0] and fr[1] < other[1]):
                stays.add(other)
                dec[to] = 'm', fr
            else:
                stays.add(fr)

    return dec, stays

N = int(raw_input())
att1, arm1 = [int(v) for v in raw_input().split()]
att2, arm2 = [int(v) for v in raw_input().split()]
dam1 = 5 + att1 - arm2
dam2 = 5 + att2 - arm1
zergs1 = {}
zergs2 = {}

switch = N **2 /10
board = [[0] * N for _ in range(N)]

ids = 1
for n in range(N):
    line = raw_input()
    for col, letter in enumerate(line):
        if letter == '1':  
            zergs1[ids] = (35, n, col)
            board[n][col] = ids
            ids += 1
        if letter == '2':  
            zergs2[ids] = (35, n, col)
            board[n][col] = ids
            ids += 1
rounds = int(raw_input())

for r in rounds:
    dec1,, stay1 = decide(zergs1, zergs2)
    dec2, stay2 = decide(zergs2, zergs1)
    for d in dec1:
        do(d, stay1, board)
    for d in dec2:
        do(d, stay1, board)
    if len(zergs1) <= 0 or len(zergs2) <= 0:
        break

for row in range(n):
    line = ''.join(board[row])
    print(line)
    