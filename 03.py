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


# Using add from array which creates already sorted arr
def merge_iter_add(arr1: arr, arr2: arr):
    p1 = arr1.first
    p2 = arr2.first
    new = arr()
    while p1 is not None:
        new.add(p1.val)
        p1 = p1.next
    while p2 is not None:
        new.add(p2.val)
        p2 = p2.next
    return new


# Using normal iter method and nodes (returns pointer to the first NODE)
def merge_iter(head1: Node, head2: Node):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    head = Node(0)
    tail = head

    while True:
        if head1 is None:
            tail.next = head2
            return head.next
        if head2 is None:
            tail.next = head1
            return head.next

        if head1.val >= head2.val:
            tail.next = head2
            head2 = head2.next
        else:
            tail.next = head1
            head1 = head1.next

        tail = tail.next


# Using recursive function
def merge_recursive(head1, head2):
    tmp = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.val <= head2.val:
        tmp = head1
        tmp.next = merge_recursive(head1.next, head2)
    else:
        tmp = head2
        tmp.next = merge_recursive(head1, head2.next)

    return tmp

A = arr()
A.add(12)
A.add(15)
A.add(17)
A.add(18)
print(A)
B = arr()
B.add(1)
B.add(14)
B.add(144)
print(B)
n = merge_recursive(A.first, B.first)
node_printer(n)
