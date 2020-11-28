import math
N = int(raw_input())
names = {0: set(['A']), 1: set(['A#', 'Bb']),2: set(['B']), 3: set(['C']),4: set(['C#', 'Db']) ,5: set(['D']),6: set(['D#', 'Eb']), 7: set(['E']), 8: set(['F']), 9: set(['F#', 'Gb']), 10: set(['G']), 11: set(['G#', 'Ab'])}
keys = {'G major': set(['G', 'A', 'B', 'C', 'D', 'E', 'F#']),
'C major': set(['C', 'D', 'E', 'F', 'G', 'A', 'B']),
'Eb major': set(['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D']),
'F# minor': set(['F#', 'G#', 'A', 'B', 'C#', 'D', 'E']),
'G minor': set(['G', 'A', 'Bb', 'C', 'D', 'Eb', 'F'])
 }
candidateKeys = set([k for k in keys])
song = []
for n in range(N):
    f = float(raw_input())
    pitchnames = names[int(round(12 * math.log(f/440.0, 2), 0)) % 12]
    filtered = set()
    song.append(pitchnames)
#    print pitchnames
    for k in candidateKeys:
        if pitchnames & keys[k]:
            filtered.add(k)
    candidateKeys = filtered
#    print candidateKeys
if len(candidateKeys) == 1:
    for k in candidateKeys: break
    print k
    for s in song:
        for n in s & keys[k]: break
        print n
else:
    print 'cannot determine key'
