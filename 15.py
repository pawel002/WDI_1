class Node:

    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


def func(x: int):
    T = [0] * 3
    while x:
        T[x % 3] += 1
        x //= 3
    return T[1] > T[2]


def delete_tri(head: Node):
    p = Node(0)
    p.next = head
    flag = True
    while p.next is not None:
        q = p.next
        while q is not None and func(q.val):
            q = q.next
        p.next = q
        if p.next is None:
            break
        p = p.next
        if flag:
            Head = q
            flag = False
    return Head


# Prints linked list
def node_printer(head: Node):
    while head is not None:
        if head.next is not None:
            print(str(head) + ", ", end="")
        else:
            print(head)
        head = head.next


A = Node(4)
B = Node(16)
C = Node(5)
D = Node(135)
A.next = B
B.next = C
C.next = D
node_printer(delete_tri(A))

