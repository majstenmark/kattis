from decimal import Decimal
import math
R = input()
r2 = Decimal(R **2)
circ = r2 * Decimal(math.pi)
sq = r2 * 2
print circ
print sq
