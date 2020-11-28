S, T, N = [int(v) for v in raw_input().split()]
D = [int(v) for v in raw_input().split()]
B= [int(v) for v in raw_input().split()]
C= [int(v) for v in raw_input().split()]

time = 0
for bus in range(N):
    #go to bus
    time += D[bus]
    #wait for bus
    k = (time + C[bus] -1)//C[bus]
    nextbus = k * C[bus]
    time = nextbus
    #ride bus
    time += B[bus]
time += D[-1]
if time<= T:
    print('yes')
else:
    print('no')