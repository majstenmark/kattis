a = raw_input()
b = raw_input()
arev = a[::-1]
brev  = b[::-1]
rest = 0
res = []
maxindex = max(len(a), len(b))
for n in range(maxindex):
    val = rest
    if n < len(a):
        val += int(arev[n])
    if n < len(b):
        val += int(brev[n])
    rest = val /10
    tmp = val % 10
    res.append(tmp)
if rest:
    res.append(rest)
value = res[::-1]
print(''.join(map(str, value)))