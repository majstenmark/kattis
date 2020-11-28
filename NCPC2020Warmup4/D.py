inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def space(col, mxr, grid):
    for i in range(mxr):
        if grid[i][col] != ' ':
            return False
    return True

def isFraction(s, e, grid):
    if R == 3:
        return grid[1][s] == '='
    return False

ops = set(['-', '*', '+'])
def isOp(s, e, grid):
    for r in range(R):
        ch = grid[r][s]
        if ch in ops:
            return True
    return False

def op(s, e, grid):
    for r in range(R):
        ch = grid[r][s]
        if ch in ops:
            return ch
    return ''    
    
def simple(s,e, r, grid):
    return grid[r][s:e]

def isSqrt(s, e, grid):
    if grid[0][e-1] == '_':
        return True
    return False

def parseSqrt(s, e, grid):
    return simple(s+2, e, 1, grid)

expr = []

R, C = nl()
grid = [inp() for _ in range(R)]
s = 0

for e in range(C):
    if space(e, R, grid):
        expr.append((s, e))
        s = e+1
expr.append((s, C))

es = []
for s, e in expr:
    if isOp(s, e, grid):
        val = op(s, e, grid)
        es.append(val)
    elif isFraction(s, e, grid):
        val1 = simple(s, e, 0, grid)
        val2 = simple(s, e, 2, grid)
        es.append('(' + val1+ ')')
        es.append('/')
        es.append('(' + val2+ ')')
    elif isSqrt(s, e, grid):
        val3 = parseSqrt(s, e, grid)
        es.append('(' + val3+ ')')
        es.append("**0.5")
    else:
        val4 = simple(s, e, R//2, grid)
        es.append('(' + val4+ ')')
r = eval(''.join(es))
print(round(r))




