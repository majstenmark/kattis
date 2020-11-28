C = int(raw_input())
for c in range(C):
    grades = [int(v) for v in raw_input().split()][1:]
    N = len(grades)
    av = sum(grades) * 1.0/N
    
    above = sum(x > av for x in grades)
    perc = above * 100.0/N
    print('{0:.3f}%'.format(perc))  