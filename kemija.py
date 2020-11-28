coded = raw_input()
out = []
vowels = set(['a', 'e', 'i', 'o', 'u'])
i = 0
while i < len(coded):
    ch = coded[i]
    out.append(ch)
    if ch in vowels:
        i += 3
    else:
        i += 1

print(''.join(out))