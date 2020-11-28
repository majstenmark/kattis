C = float(raw_input())
L = int(raw_input())

totArea = 0.0
for lawn in range(L):
    w, l = map(float, raw_input().split())
    totArea += w * l
cost = C * totArea
print(cost)
