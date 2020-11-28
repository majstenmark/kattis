A, B, C = [int(v) for v in raw_input().split()]
cnt = 0
while C -A > 2:
    
    left = B - A -1
    right = C - B - 1
    if left > right:
        A, B, C = A, A + 1, B
    else:
        A, B, C = B, C-1, C
    cnt += 1
print(cnt)