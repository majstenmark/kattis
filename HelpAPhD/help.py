N = input()
for n in range(N):
    line = raw_input()
    if line == 'P=NP':
        print 'skipped'
    else:
        print eval(line)
