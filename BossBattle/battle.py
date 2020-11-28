N = int(raw_input())
front = 0
bombs = 0
while front < N:
    bombs += 1
    front += 3
    if front >= N:
        break
    front -= 2
print(bombs)