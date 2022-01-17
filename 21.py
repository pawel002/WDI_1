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


def del_longest_increasing(head: Node):
    a = None
    b = head
    c = head.next
    maxLen = 0
    delHead = 0
    while c is not None:
        if b.val < c.val:
            currLen = 1
            p, q = b, c
            while q is not None and p.val < q.val:
                currLen += 1
                p, q = q, q.next
            if currLen > maxLen:
                maxLen = currLen
                currLen = 0
                delHead = a
        a, b, c = b, c, c.next
    if delHead == 0:
        return head
    if delHead is None:
        p = head
        for i in range(maxLen):
            p = p.next
        return p
    p = delHead.next
    for i in range(maxLen):
        p = p.next
    delHead.next = p
    return head


def node_printer(head: Node):
    while head is not None:
        if head.next is not None:
            print(str(head) + ", ", end="")
        else:
            print(head)
        head = head.next


A = LinkedList()
A.add(1)
A.add(2)
A.add(3)
A.add(4)
A.add(5)
A.add(6)
A.add(1)
A.add(2)
A.add(3)
A.add(4)
A.add(5)
node_printer(A.head)
node_printer(del_longest_increasing(A.head))

