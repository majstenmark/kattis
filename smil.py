s = input()
smiles = [':)', ';)', ':-)', ';-)']
index = []
for i in range(len(s)):
    for smile in smiles:
        if smile == s[i:i+len(smile)]:
            index.append(str(i))
print('\n'.join(index))