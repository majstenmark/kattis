def ask(page, good, bad, sections, stories):
    if stories[page] > -1:
        return stories[page]

    cnt = 0
    for way in sections[page]:
        cnt += ask(way, good, bad, sections, stories)
    stories[page] = cnt
    return cnt

T = int(raw_input())

for t in range(T):
    S = int(raw_input())
    sections = {}
    good  = []
    bad = []
    stories = [-1 for page in range(401)]
    for s in range(S):
        line = raw_input().split()
        
        if line[1] == 'favourably':
            good.append(int(line[0]))
        elif line[1] == 'catastrophically':
            bad.append(int(line[0]))
        else:
            page, ch1, ch2, ch3 = map(int, line)
            sections[page] = [ch1, ch2, ch3]
    for ending in good:
        stories[ending] = 1
    for ending in bad:
        stories[ending] = 0
    res = ask(1, good, bad, sections, stories)
    print res
