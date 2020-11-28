N = int(raw_input())
stud = [int(v) for v in raw_input().split()]
rooms = [(v, i) for i, v in enumerate(stud)]
rooms.sort(reverse = True)
su = 0
for v, i in rooms[1:]:
    su += v
if rooms[0][0] > su:
    print('impossible')
else:
    ind = [str(i+1) for v, i in rooms]
    print(' '.join(ind))