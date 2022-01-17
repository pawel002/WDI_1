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


def del_val(head: Node, value):
    prev = None
    curr = head
    while curr and curr.val < value:
        prev, curr = curr, curr.next
    if curr is None:
        return
    if curr.val == value:
        if prev is None:
            return head.next
        prev.next = curr.next
    return head


# Head1 contains sorted list
def del_repeat(head1: Node, head2: Node):
    q = head2
    count = 0
    while q:
        del_val(head1, q.val)
        q = q.next
        count += 1
    return count * 2


def node_printer(head: Node):
    while head is not None:
        if head.next is not None:
            print(str(head) + ", ", end="")
        else:
            print(head)
        head = head.next


U = Node(1)
A = Node(2)
B = Node(5)
C = Node(10)
D = Node(11)
E = Node(15)
U.next = A
A.next = B
B.next = C
C.next = D
D.next = E
node_printer(U)
print(del_repeat(U, C))

