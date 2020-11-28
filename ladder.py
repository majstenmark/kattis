import math

h, v = [int(v) for v in raw_input().split()]
rad = v * math.pi / 180
hyp = int(math.ceil(h/math.sin(rad)))
print(hyp)
