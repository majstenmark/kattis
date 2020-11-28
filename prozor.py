R,S,K=[int(v) for v in raw_input().split()]
grid = [list(raw_input()) for _ in range(R)]

def flies(r, c, K):
    cnt = 0
    for row in range(r+1, r+K-1):
        for col in range(c+1, c+K-1):
            if grid[row][col] == '*':
                cnt += 1
    return cnt

mx = 0, 0, 0
for r in range(R-K+1):
    for c in range(S - K+1):
        alt = flies(r, c,K)
        if alt > mx[0]:
            mx = (alt, r, c)
print(mx[0])
for r in range(mx[1], mx[1] + K):
    grid[r][mx[2]] = '|'
    grid[r][mx[2]+K-1] = '|'
for c in range(mx[2], mx[2] + K):
    grid[mx[1]][c] = '-'
    grid[mx[1]+K-1][c] = '-'
r, c= mx[1], mx[2]
grid[r][c] = '+'
grid[r][c+K-1] = '+'
grid[r+K-1][c+K-1] = '+'
grid[r+K-1][c] = '+'
for r in range(R):
    out = ''.join(grid[r])
    print(out)