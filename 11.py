class Node:

    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


# Ans to 10
def function(head, key):
    p = head
    prev = None
    while p is not None:
        if p.val == key:
            if p.next is not None:
                prev.next = p.next
            else:
                prev.next = None
            return
        prev, p = p, p.next
    prev.next = Node(key)


# Prints linked list
def node_printer(head: Node):
    while head is not None:
        if head.next is not None:
            print(str(head) + ", ", end="")
        else:
            print(head)
        head = head.next


A = Node(1)
A.next = Node(5)
A.next.next = Node(124)
node_printer(A)
function(A, 5624)
node_printer(A)
