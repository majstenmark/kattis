import sys

itr = (line for line in sys.stdin.read().split('\n'))
def getNext():
    line = next(itr, '')
    return line.strip()

trans = {}
line = getNext()
while line != '':
    a, b = line.split()
    trans[b] = a
    line = getNext()
out = []
line = getNext()
while line != '':
    if line in trans:
        out.append(trans[line])
    else:
        out.append('eh')
    line = getNext()
print('\n'.join(out))
