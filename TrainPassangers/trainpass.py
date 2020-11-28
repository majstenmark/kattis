C, N = map(int, raw_input().split())
passInTrain = 0
ok = True
for n in range(N):
    left, entered, waited = map(int, raw_input().split())
    if left > passInTrain:
        ok = False
        break
    passInTrain -= left
    if passInTrain + entered > C:
        ok = False
        break
    passInTrain += entered
    if passInTrain < C and waited > 0:
        ok = False
        break
    
if passInTrain != 0:
    ok = False

if ok:
    print 'possible'
else:
    print 'impossible'
