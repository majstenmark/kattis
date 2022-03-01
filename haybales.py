S = list(input())
cnt = 0


changed = set([i for i in range(len(S) - 2)])
def find(s, r):
    global cnt
    for i in range(len(S) -2):
        
        if S[i:i+3] == list(s):
            S[i] = r[0]
            S[i+1] = r[1]
            S[i+2] = r[2]
            cnt += 1
            return True
    return False

if len(S) == 3:
    if S == sorted(S):
        print(0)
        exit()
    else:
        print(1)
      
while True:
    if find('PPC', 'CPP'): continue
    elif find('PCC', 'CCP'): continue
    elif find('CPC', 'CCP'): continue
    elif find('PCP', 'CPP'): continue
    else:
        break
    
    
print(cnt)




