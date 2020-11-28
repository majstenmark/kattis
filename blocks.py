N, M = map(int, raw_input().split())
I = 1
opponent = -1


def playgame(player, n, m):
    smallest = min(n, m)
    largest = max(n, m)
    if largest % smallest == 0:
        return player == I
    if largest - smallest > smallest:
        # more than one move
        return player == I
    else:
        return playgame(-player, largest - smallest, smallest)

result = playgame(I, N, M)
if result:
    print('win')
else:
    print('lose')
