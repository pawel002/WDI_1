class Node:
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class arr:
    def __init__(self):
        self.first = None

    def add(self, value):
        p = self.first
        if p is None:
            self.first = Node(value)
            return
        if value < p.val:
            tmp = p
            self.first = Node(value)
            self.first.next = tmp
            return
        flag = True
        while p.next is not None:
            if p.val <= value < p.next.val:
                flag = False
                tmp = p.next
                p.next = Node(value)
                p.next.next = tmp
                return
            p = p.next
        if flag:
            p.next = Node(value)

    def __getitem__(self, idx):
        p = self.first
        if p is None:
            return "empty arr"
        count = 0
        while p is not None:
            if count == idx:
                return p.val
            p = p.next
            count += 1
        return "out of range"

    def __str__(self):
        a = []
        p = self.first
        while p is not None:
            a.append(p.val)
            p = p.next
        a = map(str, a)
        output = ', '.join(a)
        return output


# Prints linked list
def node_printer(head: Node):
    while head is not None:
        if head.next is not None:
            print(str(head) + ", ", end="")
        else:
            print(head)
        head = head.next


# Reverses linked list longer method
def reverse1(head: Node):
    flag = True
    while head.next is not None:
        if flag:
            head_new = head.next
            head_prev = head
            head.next = None
            flag = False
        else:
            head_new = head.next
            head.next = head_prev
            head_prev = head
        head = head_new
    head.next = head_prev
    return head


# Reversing a linked list shorter method
def reverse2(head: Node):
    prev = None
    current = head
    while current is not None:
        new = current.next
        current.next = prev
        prev = current
        current = new
    return prev


A = arr()
A.add(12)
A.add(15)
A.add(17)
A.add(18)
print(A)
n = reverse2(A.first)
node_printer(n)
