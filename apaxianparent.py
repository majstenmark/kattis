Y, P = raw_input().split()
vowels = set(['a', 'i', 'o','u'])
alt = Y + 'ex'+ P
if Y[-1] == 'e':
    alt = Y + 'x' + P
elif Y[-1] in vowels:
    alt = Y[0:-1] + 'ex' + P
elif Y[-2:] == 'ex':
    alt = Y+P
print(alt)
