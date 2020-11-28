N = int(raw_input())
alfa = 'abcdefghijklmnopqrstuvwxyz'
for n in range(N):
    line = raw_input().lower()
    letters = {chr(i):0 for i in range(ord('a'), ord('z') +1)}
    for ch in line:
        if ch in letters:
            letters[ch] += 1
    missing = []
    for i in alfa:
        if letters[i]== 0:
            missing.append(i)
    if len(missing)==0:
        print('pangram')
    else:
        print('missing {}'.format(''.join(missing)))        
