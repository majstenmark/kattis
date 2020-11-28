board =[raw_input() for _ in range(7)]
legal = 0
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(7):
    for j, ch in enumerate(board[i]):
        if ch == '.':
            for x, y in dirs:
                x2 , y2 = 2 * x, 2 * y
                if 0 <= i + x2 < 7 and 0 <= j + y2 < 7:
                    if board[i+x2][j + y2] == 'o' and board[i+x][j + y] == 'o':
                        legal += 1
print(legal)