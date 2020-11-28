levels = [0] + [5] * 10 + [4] * 5 + [3] * 5 + [2] * 5

history = raw_input()
wins = 0
rank = 25
stars = 0

for game in history:
    if game == 'W':
    #    print 'Win: rank ', rank, 'stars', stars
        wins += 1
        bonus = 1 if rank >= 6 and wins >= 3 else 0

        stars += (1 + bonus)
        if stars > levels[rank]:
            stars -= levels[rank]
            rank -= 1
            if rank == 0:
                print 'Legend'
                exit(0)
    else:
    #    print 'Loss: rank ', rank, 'stars', stars

        wins = 0
        if (rank, stars) == (20, 0):
            continue
        if 1 <= rank <= 20:
            stars -= 1
            if stars < 0:
                rank += 1
                stars = levels[rank] - 1

    #print 'and then rank ', rank, 'stars', stars

print rank
