N = int(raw_input())
for n in range(N):
    msg= raw_input()
    side = int(len(msg) ** 0.5)
    board= [['' for _ in range(side)] for _ in range(side)]
    i = 0
    for r in range(side):
        for c in range(side):
            ch = msg[i]
            i += 1
            board[r][c] = ch
    out= []
    for c in range(side -1, -1, -1):
        for r in range(side):
            ch = board[r][c]
            out.append(ch)
    print(''.join(out))