N, M = map(int, raw_input().split())
dance =[list(raw_input()) for _ in range(N)]
moves = 1
for col in range(M):
    splitter = True
    for row in range(N):
        if dance[row][col]== '$':
            splitter = False
            break
    if splitter:
        moves += 1
print(moves)