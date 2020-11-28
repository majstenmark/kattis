N = int(raw_input())
bricks = 1
side = 1
newside = side +1
while bricks + side +1 <= N:
    side += 1
    bricks += side 

print(side)

     