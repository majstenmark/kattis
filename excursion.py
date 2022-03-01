S = [int(v) for v in input()]
inv = 0
for val in range(2):
    b4 = 0
    for i in S:
        if i > val:
            b4 += 1
        if i == val:
            inv += b4
    
print(inv)
