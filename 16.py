class Node:

    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


def func(x: int):
    T = [0] * 8
    while x:
        T[x % 8] += 1
        x //= 8
    return T[5] % 2 == 0


def fives_to_front(head: Node):
    Head = head
    prev = head
    curr = prev.next
    while curr is not None:
        tmp = curr.next
        if func(curr.val):
            prev.next = tmp
            curr.next = Head
            Head = curr
        else:
            prev = curr
        curr = tmp
    return Head


# Prints linked list
def node_printer(head: Node):
    while head is not None:
        if head.next is not None:
            print(str(head) + ", ", end="")
        else:
            print(head)
        head = head.next


A = Node(7)
B = Node(2984)
C = Node(5)
D = Node(191021)
A.next = B
B.next = C
C.next = D
node_printer(fives_to_front(A))


