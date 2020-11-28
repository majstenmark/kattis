import math
#L = int(raw_input())
for i in range(1000):
    L = int(math.ceil(math.log(i +1, 10)))
    totL = L * i
    print(i, ' L ', totL)
