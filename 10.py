class Node:

    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Number:
    def __init__(self):
        self.first = None

    def set(self, num):
        head = tail = None
        for i in range(len(str(num))):
            temp = Node((num // (10 ** (len(str(num)) - i - 1)) % 10))
            if head is None:
                head = tail = temp
            else:
                tail.next = temp
            tail = temp
        self.first = head

    def reverse(self):
        prev = None
        current = self.first
        while current is not None:
            new = current.next
            current.next = prev
            prev = current
            current = new
        self.first = prev

    def __str__(self):
        char = []
        p = self.first
        while p is not None:
            char.append(p.val)
            p = p.next
        char = map(str, char)
        output = "".join(char)
        return output


def reverse(head: Node):
    prev = None
    current = head
    while current is not None:
        new = current.next
        current.next = prev
        prev = current
        current = new
    return prev


def node_printer(head: Node):
    while head is not None:
        if head.next is not None:
            print(str(head) + ", ", end="")
        else:
            print(head)
        head = head.next


# Ans to 10
def add(head1: Node, head2: Node):
    tail1 = reverse(head1)
    tail2 = reverse(head2)
    tail = Node()
    Tail = tail
    remainder = 0
    while tail1 and tail2:
        tail.next = Node((tail1.val + tail2.val + remainder) % 10)
        remainder = (tail1.val + tail2.val + remainder) // 10
        tail, tail1, tail2 = tail.next, tail1.next, tail2.next
    while tail1:
        tail.next = Node((tail1.val + remainder) % 10)
        remainder = (tail1.val + remainder) // 10
        tail, tail1 = tail.next, tail1.next
    while tail2:
        tail.next = Node((tail2.val + remainder) % 10)
        remainder = (tail2.val + remainder) // 10
        tail, tail2 = tail.next, tail2.next
    if remainder != 0:
        tail.next = Node(1)
    return reverse(Tail.next)


n = Number()
n.set(9999)
m = Number()
m.set(1423)
node_printer(add(n.first, m.first))

