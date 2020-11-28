Orig = raw_input()
After = raw_input()
correct = 0

for start in range(min(len(Orig), len(After))):
    if Orig[start] != After[start]:
        break
    else:
        correct +=1


for fromend in range(1, min(len(Orig), len(After)) + 1):
    if Orig[len(Orig) - fromend] != After[len(After) - fromend]:
        break
    else:
        correct += 1
#print fromend
#print start
correct = min(correct,len(Orig))
ins = max(0, len(After) - correct)
print ins
