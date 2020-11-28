N = int(raw_input())
dia = []
color= {}
for n in range(N):
    c = raw_input().split()
    if c[0].isdigit():
        dia.append(int(c[0]))
        color[int(c[0])] = c[1]
    else:
        dia.append(2 * int(c[1]))
        color[2 * int(c[1])] = c[0]
        
dia.sort()
for d in dia:
    print(color[d])
