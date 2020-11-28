k = int(raw_input())
mine = raw_input()
friend = raw_input()
N = len(mine)
same = len([mine[x] for x in range(N) if mine[x] == friend[x]])
diff = min(N - same, N - k)
print min(same, k) + diff
