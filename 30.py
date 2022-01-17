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


def merge_LL(head1: Node, head2: Node):
    p = head2
    while p:
        head1 = sortInsert(head1, Node(p.val))
        p = p.next
    return head1


def sortInsert(head: Node, node: Node):
    Head = head
    current = head
    prev = Node(-999999999)
    flag = False
    while current is not None and not prev.val < node.val < current.val:
        prev, current = current, current.next
        flag = True
    if not current:
        if prev.val >= node.val:
            return Head
        prev.next = node
    else:
        if flag:
            prev.next = node
            node.next = current
        else:
            Head = node
            Head.next = current
    return Head


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
node_printer(A.head)

B.add(6)
B.add(6)
B.add(0)
B.add(7)
B.add(11)
B.add(11)
B.add(11)
B.add(16)
H = merge_LL(A.head, B.head)
node_printer(H)