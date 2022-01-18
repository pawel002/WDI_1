class Node:

    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Cycle:
    def __init__(self):
        self.first = None

    def add(self, name):
        if not self.first:
            self.first = Node(name)
            self.first.next = self.first
            return
        if self.first.next == self.first:
            self.first.next = Node(name)
            self.first.next.next = self.first
            return
        p = self.first
        LOL = 1
        while p is not self.first or LOL:
            LOL = 0
            if p.val <= name <= p.next.val or (p.next.val <= p.val <= name):
                new = p.next
                p.next = Node(name)
                p.next.next = new
                self.first = p.next
                return
            p = p.next

    def print(self):
        p = self.first
        while p.val < p.next.val:
            p = p.next
        q = p.next.next
        print(p.next, end=", ")
        while q != p.next:
            print(q.val, end=", ")
            q = q.next
        return


C = Cycle()
C.add("anna")
C.add("bnna")
C.add("cnna")
C.add("dnna")
C.add("baa")
C.print()



