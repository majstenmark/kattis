LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3

def buffer(line):
    return line + [0] * (4 - len(line))

def move_line(line):
    nl = []
    tmp = []
    for d in line:
        if d > 0:
            tmp.append(d)
    
    tmp = buffer(tmp)

    if tmp[0] == tmp[1]:
        nl.append(2 * tmp[0])
        if tmp[2] == tmp[3]:
            nl.append(2 * tmp[2])
        else:
            nl.append(tmp[2])
            nl.append(tmp[3])
        
        return buffer(nl)
    nl.append(tmp[0])
    if tmp[1] == tmp[2]:
        nl.append(2 * tmp[1])
        nl.append(tmp[3])
        return buffer(nl)
    nl.append(tmp[1])
    if tmp[2] == tmp[3]:
        nl.append(2 * tmp[2])
    else:
        nl.append(tmp[2])
        nl.append(tmp[3])
    return buffer(nl)
    
        


grid= []
for row in range(4):
    line = [int(v) for v in raw_input().split()]
    grid.append(line)
move = int(raw_input())
out = [[0] * 4 for _ in range(4)]
if move == LEFT:
    for row in range(4):
        out[row] = move_line(grid[row])
if move == RIGHT:
    for row in range(4):
        line = grid[row][::-1]
        res = move_line(line)[::-1]
        out[row] = res
if move == UP:
    for c in range(4):
        line = []
        for row in range(4):
            line.append(grid[row][c])
        res = move_line(line)
        for row in range(4):
            out[row][c]= res[row]
if move == DOWN:
    for c in range(4):
        line = []
        for row in range(3, -1, -1):
            line.append(grid[row][c])
        res = move_line(line)[::-1]
        for row in range(4):
            out[row][c]= res[row]
for row in range(4):
    print(' '.join(map(str, out[row])))

            


