from math import sin, cos, pi

N = int(raw_input())
TURN = 1
WALK = 2

def walk(x, y, alpha, d):
    rad = alpha *pi/180.0
    dx = d * cos(rad)
    dy = d * sin(rad)
    return x + dx, y + dy

def follow(inst, x, y, alpha):
    for do, nbr in inst:
        if do == TURN:
            alpha += nbr
        else:
            x, y = walk(x,y, alpha, nbr)
    return x, y 

def av(goals):
    av_x = 0.0
    av_y = 0.0
    for x,y in goals:
        av_x += x
        av_y += y
    return av_x/len(goals), av_y/len(goals)

def dist(x, y, av_x, av_y):
    return ((x - av_x) ** 2 + (y - av_y) ** 2) ** 0.5

def maxdist(goals, av_x, av_y):
    mx= 0.0
    for x, y in goals:
        d = dist(x,y, av_x, av_y)
        mx = max(d, mx)
    return mx

while N != 0:
    goals = []
    for n in range(N):
        data = raw_input().split()
        x = float(data[0])
        y = float(data[1])
        start_alpha = float(data[3])
        inst = data[4:]
        todo = []
        for i in range(len(inst), 2):
            do = inst[i]
            nbr = float(inst[i+1])
            todo.append((TURN if do == 'turn' else WALK, nbr))
        goal = follow(todo, x, y, start_alpha)
        goals.append(goal)

    av_x, av_y = av(goals)
    print(goals)
    mx = maxdist(goals, av_x, av_y)    
    print('{} {} {}'.format(av_x, av_y, mx))



    N = int(raw_input())