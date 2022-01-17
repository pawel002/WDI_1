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


def Dup_counter(head: Node):
    p = Node()
    p.next = head
    count = 0
    while p.next is not None:
        if p.val == p.next.val:
            if p.next.next is None:
                p.next = None
            else:
                p.next = p.next.next
            count += 1
            continue
        p = p.next
    return count


A = LinkedList()
A.add(3)
A.add(3)
A.add(5)
A.add(5)
A.add(5)
A.add(6)
A.add(10)
A.add(10)
print(Dup_counter(A.head))
