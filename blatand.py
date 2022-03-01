left = set([s + str(i) for i in range(1, 9) for s in ['-', '+']])
right = set([str(i) + s for i in range(1, 9) for s in ['-', '+']])
N = int(input())
problem = [input().split() for _ in range(N)]
L = R = True
for tooth, issue in problem:
    if issue == 'b':
        if tooth in left: L = False 
        else: R = False
    else:
        left.discard(tooth)
        right.discard(tooth)
left_str = ''.join(left)
right_str = ''.join(right)
#Both upper and lower tooths in L
if L and '+' in left_str and '-' in left_str:
    print(0)
elif R and '+' in right_str and '-' in right_str:
    print(1)
else:
    print(2)
