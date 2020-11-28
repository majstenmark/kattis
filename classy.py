T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    li = []
    for n in range(N):
        line = raw_input().split()
        name = line[0][0:-1]
        classes = line[1].split('-')
        class_list = ['middle'] * (10 - len(classes)) + classes
        cl_to_sort = []
        for cl in class_list:
            if cl == 'middle':
                cl_to_sort.append('m')
            if cl== 'upper':
                cl_to_sort.append('a')
            if cl == 'lower':
                cl_to_sort.append('x')
        s= ''.join(cl_to_sort[::-1])
        li.append((s, name))    

    li.sort()
    for _, name in li:
        print(name)
    print('=' * 30)
        
        
