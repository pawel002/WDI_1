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


def Contains(head1: Node, head2: Node):
    p = head1
    q = head2
    while p is not None and p != q:
        p = p.next
    if p is None:
        return False
    while p or q:
        if p != q:
            return False
        p, q = p.next, q.next
    return True



