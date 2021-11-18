class Component:
    def __init__(self, x, y, colour, stones, size):
        self.stones = [(x, y)]
        self.colour = colour
        self.empties = set()
        self.alive = True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x_ = x + dx
            y_ = y + dy
            if not 0 <= x_ < size or not 0 <= y_ < size:
                continue
            if (x_, y_) not in stones:
                self.empties.add((x_,y_))


    def __str__(self):
        return f"{self.stones} [{'@' if self.colour else 'O'}] empties: {self.empties}"

class Board:
    def __init__(self, S):
        self.size = S
        self.stones = dict()
        self.component_of = dict()

    def find(self, x, y): # needed?
        if (x, y) in self.component_of:
            assert self.component_of[x,y].alive
            return self.component_of[x, y]

        return None

    def union(self, smaller, larger):
        #print("unioning", smaller, "and",  larger)
        if smaller == larger:
            return
        assert smaller.alive and larger.alive
        assert smaller.colour == larger.colour
        if len(smaller.stones) > len(larger.stones):
            smaller, larger = larger, smaller
        for x, y in smaller.stones:
            self.component_of[x, y] = larger
        larger.stones += smaller.stones
        larger.empties.update(smaller.empties)
        #print(" result", larger)
        smaller.alive = False


    def capture(self, comp) -> int:
        #assert len(comp.empties) == 0, comp
        assert comp.alive
        res = len(comp.stones)
        for x, y in comp.stones:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                other_comp = self.find(x + dx, y + dy)
                if other_comp is None:
                    continue
                other_comp.empties.add((x,y))
            del self.component_of[x,y]
            del self.stones[x, y]
        comp.alive = False
        return res


    def place(self, x, y, colour) -> int:
        # return number of captured stones caused
        # by placing x, y
        ct = 0
        self.stones[x, y] = colour
        new_comp = Component(x, y, colour, self.stones, self.size)
        self.component_of[x, y] = new_comp
        ours, theirs = set(), set()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            other_comp = self.find(x + dx, y + dy)
            if other_comp is None:
                continue
            if other_comp.colour == colour:
                ours.add(other_comp)
            else:
                theirs.add(other_comp)
        for comp in ours:
            comp.empties.remove((x, y)) # try remove instead
            new_comp = self.find(x, y) # may have changed, hence new find(!)
            self.union(new_comp, comp)
        to_capture = []
        for comp in theirs:
            if not comp.alive:
                continue
            comp.empties.remove((x,y))
            if len(comp.empties) == 0:
                to_capture.append(comp)
        #print ("To capture:", to_capture)
        if len(to_capture) == 0:
            #print (*ours)
            for comp in list(ours) + [self.find(x,y)]:
                #print ("!!", comp, comp.empties)
                if not comp.alive:
                    continue
                if len(comp.empties) == 0:
                    to_capture.append(comp)
        for comp in set(to_capture):
            ct += self.capture(comp)
        return ct

    def __str__(self):
        S = self.size
        assert S < 20
        res = []
        for x in range(S):
            line = []
            for y in range(S):
                if (x, y) in self.stones:
                    line.append('@' if self.stones[x, y] else 'O')
                else:
                    line.append(".")
            res.append("".join(line))
        return "\n".join(res)


def main():
    S, M = map(int, input().split())
    ct = 0
    board = Board(S)
    black = True
    for _ in range(M):
        x, y = map(int, input().split())
        #print("\n", "Move: ", x, y, black)
        ct += board.place(x, y, black)
        black = not black
        #print(board)

         #    for x, y in board.stones:
            #print (x, y, board.component_of[x,y])
        #print ("ct now", ct)
    print (ct)

main()
