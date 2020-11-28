N, P = map(int, raw_input().split())
stud = map(int, raw_input().split())
profit = [x - P for x in stud]
acc = [0] * N
#print profit
currProf = 0
maxProf = 0
for slot in profit:
    # either restart or continue
    if currProf + slot >= 0:
        currProf += slot
    else:
        currProf = max(0, slot)
    maxProf = max(currProf, maxProf)
print maxProf
