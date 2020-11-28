H, W, N = map(int, raw_input().split())
bricks = map(int, raw_input().split())
currW = 0

if sum(bricks) < W * H:
    print 'NO'
    exit()

bricknbr = 0
layer = 0
while bricknbr < N and layer < H:
    if currW + bricks[bricknbr] <= W:
        currW += bricks[bricknbr]
        bricknbr += 1
        if currW == W:
            currW = 0
            layer += 1
    else:
        print 'NO'
        exit()
print 'YES'
