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


def node_printer(head: Node):
    while head is not None:
        if head.next is not None:
            print(str(head) + ", ", end="")
        else:
            print(head)
        head = head.next


def Uni_sorted(head: Node):
    p = Node()
    p.next = head
    while p.next is not None:
        if p.val == p.next.val:
            if p.next.next is None:
                p.next = None
            else:
                p.next = p.next.next
            continue
        p = p.next


def LLSort(head: Node):
    p = head
    Head = Node(-999)
    while p is not None:
        Head = sortInsert(Head, Node(p.val))
        p = p.next
    return Head.next


def sortInsert(head: Node, node: Node):
    Head = head
    current = head
    prev = Node(-999999999)
    flag = False
    while current is not None and not prev.val <= node.val <= current.val:
        prev, current = current, current.next
        flag = True
    if current is None:
        prev.next = node
    else:
        if flag:
            prev.next = node
            node.next = current
        else:
            Head = node
            Head.next = current
    return Head


A = LinkedList()
A.add(3)
A.add(5)
A.add(11)
A.add(112341)
A.add(10)
# IF SORTED
Uni_sorted(A.head)
# IF NOT SORTED
B = LLSort(A.head)
node_printer(B)



