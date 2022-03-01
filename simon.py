N = int(input())
for _ in range(N):
    cmd = input()
    if cmd.startswith('simon says'):
        todo = cmd.split()[2:]
        print(' '.join(todo))
    else:
        print('')