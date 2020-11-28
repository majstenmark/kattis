import sys
from collections import Counter
names = sys.stdin.readlines()
first_names = Counter()
full_names = []
for name in names:
    first, last = name.split()
    first_names[first] += 1
    full_names.append((first, last))
full_names.sort(key = lambda x: (x[1], x[0]))
for first, last in full_names:
    if first_names[first] > 1:
        print('{} {}'.format(first, last))
    else:
        print(first)
    