class Node:

    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


def pow_change(head, st):
    p = head
    while p is not None:
        if p.val == st:
            return True
    return False

A = Node("asd")
A.next = Node("adsa")
A.next.next= Node("asdfd")
