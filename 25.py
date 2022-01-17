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


def loop_length(head: Node):
    p = head.next
    q = head.next.next
    while p != q:
        p = p.next
        q = q.next.next
        if q == p:
            start = p
    L = 1
    p = p.next
    while start != p:
        L += 1
        p = p.next
    return L


def list_len(head: Node):
    s = set()
    L = 0
    curr = head
    while curr:
        L += 1
        if curr in s:
            return L - 1
        s.add(curr)
        curr = curr.next


def tail_len(head: Node):
    Cycle_len = loop_length(head)
    List_len = list_len(head)
    return List_len - Cycle_len


def last_tail_pointer(head: Node):
    Len = tail_len(head)
    p = head
    for i in range(Len - 1):
        p = p.next
    return p


U = Node(123)
A = Node(10)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
U.next = A
A.next = B
B.next = C
C.next = D
D.next = E
E.next = B
print(last_tail_pointer(U))