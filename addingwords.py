import sys

def calc(li):
    
    res = 0
    add = True
    for v in li:
        if v in defs:
            if add:
                res += defs[v]
            else:
                res -= defs[v]
        elif v== '+':
            add = True
        elif v == '-':
            add = False
        elif v == '=':
            continue
        else:
            li.append('unknown')
            return ' '.join(li)
    if res in vals:
        li.append(vals[res])
    else:
        li.append('unknown')
    return ' '.join(li)



defs = {}
vals = {}
for line in sys.stdin.readlines():
    cmd = line.split()
    if cmd[0] == 'def':
        var = cmd[1]
        i = int(cmd[2])
        if var in defs:
            old = defs[var]
            del vals[old]
            
        defs[var] = i
        vals[i] = var
    if cmd[0] == 'calc':
        res = calc(cmd[1:])
        print(res)
    if cmd[0] == 'clear':
        defs = {}
        vals = {}
    