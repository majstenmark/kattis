import math
inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

pi = math.pi
R, C = nl()
tot = pi * R **2
I = R - C
inner = pi * I**2
proc = inner /tot * 100
print(proc)