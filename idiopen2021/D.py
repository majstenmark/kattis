from collections import *
try: inp = raw_input
except: inp = input
def ni(): return int(inp())
def nl(): return [int(x) for x in inp().split()]

a, b, c, d = nl()

ops = ['*', '+', '-', '/']

outs = []
for op1 in ops:
    for op2 in ops:
        exp = '{} {} {} == {} {} {}'.format(a, op1, b, c, op2, d)
        try:
            if eval(exp):
                outs.append(exp.replace('==', '='))
        except: pass
if len(outs):
    print('\n'.join(outs))
else:
    print('problems ahead')