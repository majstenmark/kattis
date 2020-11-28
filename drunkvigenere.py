msg = raw_input()
key = raw_input()

A = ord('A')
out = []
for i, ch in enumerate(msg):
    shift = ord(key[i]) - A
    index = ord(ch) - A
    if i % 2 == 0:
        #shift backward
        diff = (index - shift) % 26
        dec = chr(A + diff)
        out.append(dec)
        
    else:
        #shift forward
        diff = (index + shift) % 26
        dec = chr(A + diff)
        out.append(dec)
print(''.join(out))
