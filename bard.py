def nl():
    return [int(v)-1 for v in input().split()]

N = int(input())
E = int(input())
eve = [nl()[1:] for _ in range(E)]
knows = [set() for _ in range(N)]
song_no = 0
for li in eve:
    if 0 in li:
        #print('bard', li)
        for v in li:
            knows[v].add(song_no)
        song_no += 1
        
    else:
        all = set()
        for v in li:
            all |= knows[v]
        for v in li:
            knows[v] = set(all)
    #print(knows)
all = set()
for v in range(1, N):
    all |= knows[v]
knows_all = ['1']
#print(knows)
for v in range(1, N):
    if len(all & knows[v]) == len(all):
        knows_all.append(str(v+1))
print('\n'.join(knows_all))
        

