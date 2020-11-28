sides = [int(v) for v in raw_input().split()]
sides.sort()
print(sides[0]* sides[2])