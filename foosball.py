from collections import deque

def won(wino, wind, losto, lostd):
        wino, wind = wind, wino
        out = lostd
        lostd = losto
        rest.append(out)
        losto = rest.popleft()
        return wino, wind, losto, lostd
        

N = int(raw_input())
players = raw_input().split()
wo, bo, wd, bd = players[0], players[1], players[2], players[3]
wonlast = ''
rest = deque(players[4:])
curr = 0
streak = []
white = wo, wd
black = bo, bd

games = raw_input()
for g in games:
    if g == 'W':
        if wonlast == g:
            #add streak point
            curr += 1
        else:
            #did not win last time
            streak.append((black, curr))
            curr = 1
        wo, wd, bo, bd = won(wo, wd, bo, bd)
        black = (bd, bo)
        
    else: 
        #black won
        if wonlast == g:
            #add streak point
            curr += 1
        else:
            streak.append((white, curr))
            curr  = 1

        bo, bd, wo, wd = won(bo, bd, wo, wd)
        white = (wd, wo)
    wonlast = g
#last, save the current winner
if wonlast == 'W':
    streak.append((white, curr))
else:
    streak.append((black, curr))
mx = 0
for team, s in streak:
    mx = max(mx, s)
for team, s in streak:
    if s == mx:
        print('{} {}'.format(team[0], team[1]))



