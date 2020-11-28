def p():
    print(' ').join(map(str, P))

P = [int(v) for v in raw_input().split()]

while True:
    if P[0]>P[1]:
        P[0], P[1]= P[1], P[0]
        p()
        
    if P[1]>P[2]:
        P[1], P[2]= P[2], P[1]
        p()

    if P[2]>P[3]:
        P[2], P[3]= P[3], P[2]
        p()

    if P[3]>P[4]:
        P[3], P[4]= P[4], P[3]
        p()
    
    if P == [1, 2, 3, 4,5]:
        exit()



