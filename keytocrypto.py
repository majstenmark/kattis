def decode(c, k):
    asc = (ord(c) - ord(k)) % 26 + ord('A')
    return chr(asc)

C = raw_input()
key = list(raw_input())
msg = []
for i in range(len(C)):
    c = C[i]
    k = key[i]
    dec = decode(c, k)
    msg.append(dec)
    key.append(dec)
print(''.join(msg))
