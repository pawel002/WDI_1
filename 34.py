from random import random
class Node:

    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Cycle:
    def __init__(self):
        self.first = None

    def add(self, val: int):
        if not self.first:
            self.first = Node(val)
            self.first.next = self.first
            return
        if self.first.next == self.first:
            self.first.next = Node(val)
            self.first.next.next = self.first
            return
        new = self.first.next
        self.first.next = Node(val)
        self.first.next.next = new

    def print(self):
        p = self.first.next
        print(self.first.val, end=", ")
        while p is not self.first:
            print(p.val, end=", ")
            p = p.next

    def D(self, k):
        Key_val = []


C = Cycle()
C.add(12)
C.add(121243)
C.add(126)
C.add(124)
C.add(1245)
C.print()
