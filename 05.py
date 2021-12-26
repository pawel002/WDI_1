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


# Extracts digits and merges them
def sort_by_last_digit(head: Node):
    # Creates heads
    heads = [Node(0) for _ in range(10)]
    # Creates tails
    tails = [heads[i] for i in range(10)]
    while head is not None:
        for i in range(10):
            if head.val % 10 == i:
                tails[i].next = head
                tails[i] = tails[i].next
                break
        head = head.next
    # If possible moves heads +1
    Heads = [head.next if head.next is not None else None for head in heads]
    # Ends all tails
    for tail in tails:
        tail.next = None
    flag = True
    # Creates head and tail for merged lists
    Head = Node()
    Tail = Node()
    # Merges lists
    for i in range(1, 9):
        if Heads[i] is not None and flag:
            Head = Heads[i]
            Tail = tails[i]
            flag = False
        if Heads[i] is not None and not flag:
            Tail.next = Heads[i]
            Tail = tails[i]
    return Head


A = arr()
A.add(12)
A.add(15)
A.add(235)
A.add(13245)
A.add(17)
A.add(18)
n = sort_by_last_digit(A.first)
node_printer(n)
