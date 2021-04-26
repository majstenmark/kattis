unique23 = set()
solved = set()

with open('distracted.txt', 'r') as f:
    lines = f.read().split('\n')
    for line in lines:

        if len(line) > 0 and 'Accepted' in line:
            data = line.split()
            first, last = data[2], data[3]
            name = first+ ' ' + last
            solved.add(name)
        if len(line) > 0 and 'Accepted (23)' in line:
            data = line.split()
            first, last = data[2], data[3]
            name = first+ ' ' + last
            unique23.add(name)
print(len(unique23))
print(len(solved))