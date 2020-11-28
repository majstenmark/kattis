li = map(int, raw_input().split())
li.sort()
A, B, C  = li

d = {'A': A, 'B': B, 'C': C}
order = raw_input()
s = []
for letter in order:
    s.append(str(d[letter]))
print ' '.join(s)
