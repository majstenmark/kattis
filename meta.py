import sys
defs = {}

def test(v1, op, v2):
    if op== '<':
        return v1 < v2
    if op == '>':
        return v1 > v2
    else:
        return v1 == v2

for l in sys.stdin.readlines():
    line = l.split()
    if line[0] == 'define':
        i = int(line[1])
        var = line[2]
        defs[var] = i
    else:
        
        v1 = line[1]
        v2 = line[3]
        op = line[2]
        if v1 not in defs or v2 not in defs:
            print('undefined')
            continue
        val1 = defs[v1]
        val2 = defs[v2]
        res = test(val1, op, val2)
        if res:
            print('true')
        else:
            print('false')
