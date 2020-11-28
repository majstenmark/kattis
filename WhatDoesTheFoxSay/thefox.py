def filter(animals, rec):
    sounds = set()
    for animal in animals:
        sounds.add(animal)
    fox = []
    for word in rec:
        if word not in sounds:
            fox.append(word)
    return ' '.join(fox)
T = input()
for t in range(T):
    recording = raw_input().split()
    animals = []

    animal = raw_input()
    while(animal != 'what does the fox say?'):
        sound = animal.split('goes')[1].strip()
        animals.append(sound)
        animal = raw_input()
    res = filter(animals, recording)
    print res
