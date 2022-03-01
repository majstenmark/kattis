import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def ni(): return int(inp())
def ops():
    data = inp().split()
    return int(data[0]), data[1], int(data[2])

N = ni()
operations = [ops() for _ in range(N)]
prev = 1
out = []
for a, op , b in operations:
    if op == '+':
        val = a + b
        prev = val - prev
    if op == '-':
        val = a - b
        prev *= val
    if op == '*':
        val = a * b
        prev = val * val
    if op == '/':
        prev = (a + 1)//2
    out.append(str(prev))
print('\n'.join(out))
