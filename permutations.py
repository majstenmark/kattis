S = 'ABC'

def perm(s, pos):
    if pos == len(s):
        print(s)
    for i in range(pos, len(s)):
        li = s[0:pos] + s[i] + s[pos:i] + s[i+1:]
        #print('Taking out', s[i],'front', s[pos:i], 'end', s[i+1:-1])
        perm(li, pos + 1)

perm(S, 0)