class Node:

    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class LL:
    def __init__(self):
        self.first = None

    def add(self, val):
        if self.first is None:
            self.first = Node(val)
        else:
            p = self.first
            while p.next:
                p = p.next
            p.next = Node(val)


def reverse(head: Node):
    prev = None
    current = head
    while current is not None:
        new = current.next
        current.next = prev
        prev = current
        current = new
    return prev


# Similar to 10, h1 - h2
def sub(head1: Node, head2: Node):
    tail1 = head1
    tail2 = head2
    tail = Node()
    Tail = tail
    while tail1 and tail2:
        tail.next = Node(tail1.val - tail2.val)
        tail, tail1, tail2 = tail.next, tail1.next, tail2.next
    while tail1:
        tail.next = Node(tail1.val)
        tail, tail1 = tail.next, tail1.next
    while tail2:
        tail.next = Node(tail2.val)
        tail, tail2 = tail.next, tail2.next
    return Tail.next


def node_printer(head: Node):
    while head is not None:
        if head.next is not None:
            print(str(head) + ", ", end="")
        else:
            print(head)
        head = head.next


L = LL()
L.add(1)
L.add(54)
L.add(6)
L.add(1)

U = LL()
U.add(12)
U.add(51)
node_printer(sub(L.first, U.first))

