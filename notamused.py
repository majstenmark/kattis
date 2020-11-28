import sys
from collections import defaultdict as dd

itr = (line for line in sys.stdin.readlines())
day = 0
try:
    while True:
        event = next(itr).split()
        day += 1
        ppl = {}
        exited = dd(int)

        while event[0] != 'CLOSE':
            if event[0] == 'ENTER':
                name = event[1]
                time = int(event[2])
                ppl[name] = time
            if event[0] == 'EXIT':
                name = event[1]
                time = int(event[2])
                exited[name] += (time - ppl[name])
            event = next(itr).split()
        
        li = [(name, 0.1 * time) for (name, time) in exited.items()]
        li.sort()
        print('Day {}'.format(day))
        for name, cost in li:
            print('{} ${:.2f}'.format(name, cost))
        print('\n')
                    
except:
    exit()