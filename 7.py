class Node:
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.first = None

    # Answer 6
    def add_end(self, val):
        tail = self.first
        if tail is None:
            self.first = Node(val)
            return
        while tail.next is not None:
            tail = tail.next
        tail.next = Node(val)

    # Answer 7
    def del_end(self):
        tail = self.first
        if tail.next is None:
            self.first = None
            return

        while tail.next.next is not None:
            tail = tail.next
        tail.next = None

    def __str__(self):
        L = []
        p = self.first
        while p is not None:
            L.append(p.val)
            p = p.next
        L = map(str, L)
        output = ', '.join(L)
        return output


A = LinkedList()
A.add_end(14)
A.add_end(15)
A.add_end(151)
print(A)
A.del_end()
print(A)

