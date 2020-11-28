from collections import defaultdict as dd

N = int(raw_input())
cnt = 1
while N:
    animals = dd(int)
    for n in range(N):
        animal = raw_input().split()[-1].lower()
        animals[animal] += 1
    sorted_animals = sorted(animals.items())
    print('List ' + str(cnt) + ':')
    for animal, count in sorted_animals:
        print('{} | {}'.format(animal, count))
    cnt += 1
    N = int(raw_input())

