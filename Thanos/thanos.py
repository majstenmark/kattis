N = int(raw_input())
ai = map(int, raw_input().split())
kills = 0
pop_allowed = ai[-1] -1
for world in ai[-2::-1]:
    pop = min(world, pop_allowed)
    kills += world - pop
    #print('killed  {} {} {}'.format(world, pop_allowed, world - pop))
    pop_allowed = pop -1
    
    if(pop < 0):
        print(1)
        exit()
print(kills)
