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
    
    # Ans to 9
    def add1(self):
        self.reverse()
        p = self.first
        remainder = 1
        while p is not None:
            if remainder == 0:
                self.reverse()
                return
            p.val, remainder = (p.val + remainder) % 10, (remainder + p.val) // 10
            if p.next is None:
                p.next = Node(1)
                break
            p = p.next
        self.reverse()

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


n = Number()
n.set(9999)
print(n)
n.add1()
print(n)
