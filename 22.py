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


def loop_finder(head: Node):
    s = set()
    curr = head
    while curr:
        if curr in s:
            return True
        s.add(curr)
        curr = curr.next
    return False