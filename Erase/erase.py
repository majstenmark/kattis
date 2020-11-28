N = input()
orig = raw_input()
output = orig
deleted = raw_input()
if N % 2 == 1:
    a = ['1' if x == '0' else '0' for x in orig]
    output = ''.join(a)
if deleted == output:
    print 'Deletion succeeded'
else:
    print 'Deletion failed'
