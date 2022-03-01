import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def nl1(): return [int(v)-1 for v in inp().split()]
def ni(): return int(inp())
def fac():
    data = nl1()
    cells = []
    for i in range(1, len(data), 2):
        r = data[i]
        c = data[i+1]
        cells.append((r, c))
    return cells




R, C, F, S, G = nl()
cells = []
for _ in range(F):
    f = fac()
    cells.append(f)
students = [nl1() for _ in range(S)]
facstudents = [[] for _ in range(F)]
for r, c, id, f in students:
    facstudents[f].append((id, r, c))

T  = nl()    
cnt = 0

def solve(pos, students, t):
    pos.sort()
    students.sort()
    ok = 0
    distances = []
    for i in range(min(len(pos), len(students))):
        desired = pos[i]
        curr = students[i][1], students[i][2]
        dist = abs(desired[0] - curr[0]) + abs(desired[1] - curr[1])
        distances.append(dist)
    distances.sort()
    return sum(distances[0:t])


moves = []
#print(cells)
#print(facstudents)
for f in range(F):
    move = solve(cells[f], facstudents[f], T[f])
    moves.append(move)
moves.sort()
cnt = sum(moves[0:G])
print(cnt)

