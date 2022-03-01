morse = {'A': '.-', 'B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.',
'H':'....', 'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.',
'O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-',
'V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..', '_':'..--', ',':'.-.-', '.':'---.', '?':'----'}
backwards = {c: m for m, c in morse.items()}

import sys
lines = sys.stdin.readlines()

def decode(line):
    numbers = []
    S = []
    for lt in line:
        m = morse[lt]
        L = len(m)
        numbers.append(L)
        S.append(m)
    rev = numbers[::-1]
    T = ''.join(S)
    msg = []
    index = 0
    for no in rev:
        s = T[index: index + no]
        msg.append(backwards[s])
        index += no
    return ''.join(msg)

for line in lines:
    msg = decode(line.strip())
    print(msg)
