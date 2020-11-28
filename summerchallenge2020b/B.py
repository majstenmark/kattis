fr, to, other = raw_input().split()
N, S, E, W = 'North','South','East','West'
RIGHT = {S: E, E: N, N: W, W:S}
LEFT = {S: W, E: S, N: E, W:N}

OPP = {N: S, S: N, W:E, E:W}

def vaj(fr, to, other):
    #straight
    if OPP[fr] == to and RIGHT[fr] == other:
        return True
    if LEFT[fr] == to and (RIGHT[fr] == other or OPP[fr] == other):
        return True
    return False

if vaj(fr, to, other):
    print('Yes')
else:
    print('No')
