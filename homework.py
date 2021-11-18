s = input()
pint = s.split(';')
cnt = 0
for i in pint:
    if '-' in i:
        a, b = map(int, i.split('-'))
        cnt += (b-a +1)
    else:
        cnt += 1
print(cnt)