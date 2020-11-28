N = int(raw_input())
wt = [int(raw_input()) for _ in range(N)]
W = sum(wt)//2
K = [[0 for x in range(W + 1)] for x in range(N + 1)] 
  
K[0][0] = 1
for i in range(1, N + 1): 
    for w in range(W + 1):
        for p in range(N//2+2):
            if (1<<p) & K[i-1][w]:
                K[i][w] |= 1<<p
                if wt[i-1] + w <= W and p*2 < N:
                    K[i][w + wt[i-1]] |= 1<<(p+1)
             
for we in range(W, -1, -1):
    nh = N//2 
    nh2 = (N+1)//2  
    if (1<<nh2 & K[-1][we]) or (1<<nh & K[-1][we]):
        print('{} {}'.format(we, sum(wt)- we)) 
        exit()



    