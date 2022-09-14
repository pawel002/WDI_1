class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


    def __str__(self):
        return str(self.val)


class LL:
    def __init__(self):
        self.first = None

    def add(self, val):
        if self.first is None:
            self.first = Node(val)
            return
        p = self.first
        while p.next is not None:
            p = p.next
        p.next = Node(val)


def repair(head: Node):
    count = 0
    curr = head
    new = head.next
    q = new.val / curr.val
    negative = False
    # Finding q
    while new is not None:
        q_new = new.val / curr.val
        if abs(1 - abs(q_new)) < abs(1 - abs(q)):
            q = q_new
        if q_new < 0:
            negative = True
        curr, new = new, new.next
    if negative:
        q = -abs(q)
    # Repairing
    curr = head
    new = head.next
    while new is not None:
        if new.val / curr.val != q:
            insert = Node(curr.val * q)
            curr.next = insert
            insert.next = new
            curr = insert
            count += 1
            continue
        curr, new = new, new.next
    return head


def node_printer(head: Node):
    while head is not None:
        if head.next is not None:
            print(str(head) + ", ", end="")
        else:
            print(head)
        head = head.next


L = LL()
L.add(-27)
L.add(-3)
L.add(1)
A = repair(L.first)
node_printer(L.first)

