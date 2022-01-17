class Intervals:
    def __init__(self):
        self.list = list()

    def add(self, val1, val2):
        self.list.append([val1, val2])

    def reduce(self):
        self.list.sort(key=lambda x: x[0])
        Open = self.list[0][0]
        Close = self.list[0][1]
        newList = []
        for i in range(1, len(self.list)):
            if Close < self.list[i][0]:
                newList.append([Open, Close])
                Open = self.list[i][0]
                Close = self.list[i][1]
            else:
                Close = max(Close, self.list[i][1])
        newList.append([Open, Close])
        self.list = newList

    def print(self):
        print(self.list)


I = Intervals()
I.add(2, 5)
I.add(90, 100)
I.add(5, 56)
I.print()
I.reduce()
I.print()