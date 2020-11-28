N,  M = map(int, raw_input().split())
better = set()
scores = [(0, 0) for _ in range(N+1)]
solved = 0
penalty = 0
for e in range(M):
    t, p = map(int, raw_input().split())
    if t != 1:
        ps, pp = scores[t]
        scores[t] = (ps + 1, pp + p)
        if scores[t][0] > solved or (scores[t][0] == solved and scores[t][1] < penalty):
            better.add(t)
    else:
        solved, penalty = solved + 1, penalty + p

        nbetter = set()
        for team in better:
            if scores[team][0] > solved or (scores[team][0] == solved and scores[team][1] < penalty):
                nbetter.add(team)
        better = nbetter
    print len(better) +1
