R, C = [int(v) for v in raw_input().split()]

letters = []
for r in range(R):
    line = raw_input()
    letters.append(line)
V = int(raw_input())
V %= 360
if V == 0:
    for line in letters:
        print(line)
    exit()
if V == 90:
    for c in range(C):
        line = []
        for r in range(R-1, -1, -1):
            line.append(letters[r][c])
        print(''.join(line))
    exit()
if V == 180:
    for r in range(R -1, -1, -1):
        line = []
            
        for c in range(C-1, -1, -1):
            line.append(letters[r][c])
        print(''.join(line))
    exit()
if V == 270:
    for c in range(C-1, -1, -1):
        line = []
        for r in range(R):
            line.append(letters[r][c])
        print(''.join(line))
    exit()
if V == 45:
    lines = [[' ' for _ in range(R + C -1)] for _ in range(R + C -1)]
    for r in range(R):
        x_offs = R - r - 1
        y_offs = r
        
        for c in range(C):
            ch = letters[r][c]
            x = x_offs + c
            y = y_offs + c
            #print('{} {} {} {}'.format(letters[r], ch, x, y))
            lines[y][x] = ch
    for i in range(R + C -1):
        L = ''.join(lines[i])
        print(L)
if V == 135:
    lines = [[' ' for _ in range(R + C -1)] for _ in range(R + C -1)]
    END = R + C -2
    for r in range(R):
        x_offs = r
        y_offs = R - 1 - r
        
        for c in range(C):
            ch = letters[r][c]
            x = END - x_offs - c
            y = y_offs + c
            #print('{} {} {} {}'.format(letters[r], ch, x, y))
            lines[y][x] = ch
    for i in range(R + C -1):
        L = ''.join(lines[i])
        print(L)

if V == 225:
    lines = [[' ' for _ in range(R + C -1)] for _ in range(R + C -1)]
    END = R + C -2
    for r in range(R):
        x_offs = R -1 -r
        y_offs = r
        
        for c in range(C):
            ch = letters[r][c]
            x = END - x_offs - c
            y = END - y_offs - c
            #print('{} {} {} {}'.format(letters[r], ch, x, y))
            lines[y][x] = ch
    for i in range(R + C -1):
        L = ''.join(lines[i])
        print(L)

if V == 315:
    lines = [[' ' for _ in range(R + C -1)] for _ in range(R + C -1)]
    END = R + C -2
    for r in range(R):
        x_offs = r
        y_offs = R -1 - r
        
        for c in range(C):
            ch = letters[r][c]
            x = x_offs + c
            y = END - y_offs - c
            #print('{} {} {} {}'.format(letters[r], ch, x, y))
            lines[y][x] = ch
    for i in range(R + C -1):
        L = ''.join(lines[i])
        print(L)


        
