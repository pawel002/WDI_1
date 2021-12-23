class Node:
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Zbior:
    def __init__(self):
        self.first = None

    def find(self, x):
        p = self.first
        while p.val < x:
            p = p.next
        return p.val == x

    def add(self, x):
        p = self.first
        q = None
        while p is not None and p.val < x:
            q = p
            p = p.next
        if p is not None and p.val == x:
            return
        tmp = Node(x)
        tmp.next = p
        if q is not None:
            q.next = tmp
            return
        self.first = tmp

    def __str__(self):
        lista = []
        p = self.first
        while p is not None:
            lista.append(p.val)
            p = p.next
        lista = map(str, lista)
        output = ', '.join(lista)
        return output


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    print(node1)
    zbior1 = Zbior()
    zbior1.add(1)
    zbior1.add(4)
    zbior1.add(2)
    zbior1.add(3)
    print(zbior1)
