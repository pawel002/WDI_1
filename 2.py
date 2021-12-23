class Node:
    def __init__(self, pos, x=None):
        self.val = x
        self.pos = pos
        self.next = None

    def __str__(self):
        return str(self.val)


class sparse_array:
    def __init__(self):
        self.first = None

    def __setitem__(self, idx, value):
        p = self.first
        if p is None:
            self.first = Node(idx, value)
            return
        if idx < self.first.pos:
            tmp = self.first
            self.first = Node(idx, value)
            self.first.next = tmp
            return
        flag = True
        while p.next is not None:
            if p.pos <= idx < p.next.pos:
                flag = False
                if p.pos == idx:
                    p.val = value
                    return
                else:
                    tmp = p.next
                    p.next = Node(idx, value)
                    p.next.next = tmp
                    return
            p = p.next
        if flag:
            p.next = Node(idx, value)

    def __getitem__(self, idx):
        p = self.first
        while p.next is not None:
            if p.pos == idx:
                return p.val
            p = p.next
        return 0

    def __str__(self):
        arr = []
        p = self.first
        while p is not None:
            arr.append(p.val)
            p = p.next
        arr = map(str, arr)
        output = ', '.join(arr)
        return output


A = sparse_array()
A[2] = 5
print(A)
A[5] = 10
A[3] = 6
print(A[3])
