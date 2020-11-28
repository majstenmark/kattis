S = raw_input()
S1 = raw_input()
S2= raw_input()
states = set()
states.add((0, 0))
for n in range(len(S)):
    states2 = set()
    for index1,index2 in states:
        if index1 < len(S1) and S[n] == S1[index1]:
            states2.add((index1 + 1, index2))

        if index2 < len(S2) and S[n] == S2[index2]:
            states2.add((index1, index2 + 1))
    states = states2
if len(states):
    print 'yes'
else:
    print 'no'
