class Node:

    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(value)


def fun(head: Node):
    Head1 = Node(0)
    p1 = Head1
    Head2 = Node(0)
    p2 = Head2
    p = head
    while p:
        if p.val > 0 and p.val % 2 == 0:
            p1.next = p
            p1 = p1.next
        if p.val < 0 and p.val % 2 == 1:
            p2.next = p
            p2 = p2.next
        p = p.next
    p1.next = None
    p2.next = None
    return Head1.next, Head2.next


def node_printer(head: Node):
    while head is not None:
        if head.next is not None:
            print(str(head) + ", ", end="")
        else:
            print(head)
        head = head.next


A = LinkedList()
A.add(-1)
A.add(-5)
A.add(8)
A.add(12)
A.add(-11)
A.add(11)
A.add(14)
A.add(-14)
A.add(16)
node_printer(A.head)
a, b = fun(A.head)
node_printer(a)
node_printer(b)