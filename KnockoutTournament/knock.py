import math

def playoff(branch):
    fights = []
    for n in range(len(branch), 2):
        fights.append([branch[n], branch[n+1]])
    if len(brnach) %2 != 0:
        fights.append([branch[-1]])
    while len(fights) > 1:
        nextfinal = []
        probs = {}
        

N = int(raw_input())
players = [int(raw_input()) for _ in range(N)]
others = players[1:]
others.sort(reverse=True) + [players[0]]
    
uplog = (N -1).bit_length()
upper =2 ** uplog
lower = 2 ** int(math.log(N + 1, 2))

#print('{} {}'.format(upper, lower))

dales_side = lower //2
other_side = N - dales_side
#print('{} {}'.format(dales_side, other_side))
other_branch = others[:other_side]
dales_branch = others[other_side:]


