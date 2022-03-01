N = int(input())
odd = []
for i in range(N):
    word = input()
    if i%2 == 0:
        odd.append(word)
print('\n'.join(odd))