from collections import Counter

phrase = raw_input().split()
words = Counter()
for w in phrase:
    words[w] += 1
for k in words:
    if words[k] > 1:
        
        print('no')
        exit()
print('yes')