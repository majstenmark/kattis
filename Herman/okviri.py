word = raw_input()
w = 5 + 4 * (len(word)-1)
grid = [['.'] * w for _ in range(5)]
for index, letter in enumerate(word):
    mid = 4 * index + 2
    grid[2][mid] = letter
    if (index +1) % 3 != 0:
        grid[0][mid] = grid[1][mid-1] = grid[1][mid+1] = grid[2][mid-2] = grid[2][mid+2] = grid[3][mid-1]= grid[3][mid+1] = grid[4][mid] = '#'
for index, letter in enumerate(word):
    mid = 4 * index + 2
    if (index +1) % 3 == 0:
        grid[0][mid] = grid[1][mid-1] = grid[1][mid+1] = grid[2][mid-2] = grid[2][mid+2] = grid[3][mid-1]= grid[3][mid+1] = grid[4][mid] = '*'


s = '\n'.join([''.join(line) for line in grid])
print s
