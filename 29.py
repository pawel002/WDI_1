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


def del_count(head1: Node, head2: Node):
    p1 = head1
    p2 = head2
    del_num = 0
    while p1 and p2:
        if p1.val == p2.val:
            p1, p2 = p1.next, p2.next
            continue
        if p1.val < p2.val:
            p1 = p1.next
            del_num += 1
            continue
        if p1.val > p2.val:
            p2 = p2.next
            del_num += 1
            continue
    while p1:
        del_num += 1
    while p2:
        del_num += 1
    return del_num


def del_nodes(head1: Node, head2: Node):
    Head1 = head1
    p1 = head1
    q1 = None
    Head2 = head2
    p2 = head2
    q2 = None
    while p1 and p2:
        if p1.val == p2.val:
            q1, p1, q2, p2 = p1, p1.next, p2, p2.next
            continue
        if p1.val < p2.val:
            if q1 is None:
                Head1 = p1.next
            else:
                q1.next = p1.next
            p1 = p1.next
            continue
        if p1.val > p2.val:
            if q2 is None:
                Head2 = p2.next
            else:
                q2.next = p2.next
            p2 = p2.next
            continue
    if p1 is not None:
        p1.next = None
    if p2 is not None:
        p2.next = None
    return Head1, Head2


def node_printer(head: Node):
    while head is not None:
        if head.next is not None:
            print(str(head) + ", ", end="")
        else:
            print(head)
        head = head.next


A = LinkedList()
B = LinkedList()
A.add(1)
A.add(5)
A.add(8)
A.add(12)
A.add(14)
A.add(16)

B.add(4)
B.add(5)
B.add(8)
B.add(11)
B.add(16)
a, b = del_nodes(A.head, B.head)
node_printer(b)

