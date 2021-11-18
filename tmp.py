out = []
for lt in 'Maj Stenmark':
    asc = ord(lt)
    out.append(bin(asc)[2:])
print(''.join(out))