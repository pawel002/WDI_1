class Node:

    def __init__(self, x=None):
        self.val = x
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.val)


class DoubleLink:
    def __init__(self):
        self.first = None
        self.last = None

    def addFirst(self, val):
        if self.first is None:
            self.first = Node(val)
            self.last = self.first
            return
        tmp = self.first
        self.first = Node(val)
        self.first.prev, tmp.next = tmp, self.first

    def addLast(self, val):
        if self.last is None:
            self.last = Node(val)
            self.first = self.last
            return
        tmp = self.last
        self.last = Node(val)
        self.last.next, tmp.prev = tmp, self.last

    def printFromHead(self):
        p = self.first
        while p is not None:
            print(str(p.val) + ", ", end="")
            p = p.prev

    def printFromTail(self):
        p = self.last
        while p is not None:
            print(str(p.val) + ", ", end="")
            p = p.next


L = DoubleLink()
L.addFirst(12)
L.addFirst(12)
L.addFirst(11)
L.printFromHead()
