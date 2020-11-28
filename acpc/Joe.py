T = 1
state = 0
CAN = set([tuple(['joe'])])
data = []
sentence = []
delim = set(['.', ',', ':', ';', '!', '?'])
testdata = []
N = 0

def addsent(sentence):
    for startindex in range(0, len(sentence)):
        for n in range(1, N+1):
            if startindex + n <= len(sentence):
                CAN.add(tuple(sentence[startindex:startindex + n]))

def testsent(sentence):
    failed = False
    #print 'Sentence ', sentence
    for n in range(1, N+ 1):
        for startindex in range(0, len(sentence)):
            if startindex + n <= len(sentence):
                origGram = tuple(sentence[startindex:startindex + n])
                grams = tuple(map(lambda x: x.lower(), sentence[startindex:startindex + n]))

                if grams not in CAN:

                    if len(grams) == 1:
                        print 'What does the word "{}" mean?'.format(str(origGram[0]))
                        failed = True
                        CAN.add(grams)
                    else:
                        addsent(sentence)
                        return True

    return failed


import sys
for l in sys.stdin.read().split():

    if state == 0:
        N = int(l)
        state = 1
        sentence = []
    elif state == 1:
        if l == '*':
            state = 2
            print('Learning case {}'.format(T))
            #print data
            data.append(sentence)
            for sentence in data:
                for startindex in range(0, len(sentence)):
                    for n in range(1, N+1):
                        if startindex + n <= len(sentence):
                            CAN.add(tuple(sentence[startindex:startindex + n]))
            #print CAN
            data = []
            sentence = []
            continue
        # read
        # learnt senteces
        if l in delim:
            data.append(sentence)
            sentence = []
        else:
            sentence.append(l.lower())

    else:
        if l == '#':

            testdata.append(sentence)
        #    print testdata
            for sentence in testdata:
                if testsent(sentence) and len(sentence) > 1:
                    print 'What does the sentence "{}" mean?'.format(' '.join(sentence))

            CAN = set([tuple(['joe'])])
            T += 1
            state = 0
            testdata = []

            print('')
            continue
        #testing
        if l in delim:
            testdata.append(sentence)
            sentence = []
        else:
            sentence.append(l)
