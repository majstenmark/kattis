
class Node:
    def __init__(self, lt, prev, nxt):
        self.letter = lt
        self.prev = prev
        self.nxt = nxt
        if prev != None:
            prev.nxt = self
        if nxt != None:
            nxt.prev = self

    
    def delete(self):
        if self.prev != None:
            self.prev.nxt = self.nxt
        if self.nxt != None:
            self.nxt.prev = self.prev
        return self.prev

    def insertAfter(self, lt):
        node = Node(lt, self, self.nxt)
        return node
    
    def insertBefore(self, lt):
        node = Node(lt, self.prev, self)
        return node
    

I = input()
N = len(I)
first = Node('', None, None)
last = Node('', first, None)
curr = first
for ch in I:
    if ch == 'B':
        curr = curr.delete()
    elif ch == 'L':
        curr = curr.prev
    elif ch == 'R':
        curr = curr.nxt
    else:
        if curr == first:
            curr = first.insertAfter(ch)
        elif curr == last:
            curr = last.insertBefore(ch)
        else:
            curr = curr.insertAfter(ch)
out = []
node = first
while node != last:
    out.append(node.letter)
    node = node.nxt
print(''.join(out))