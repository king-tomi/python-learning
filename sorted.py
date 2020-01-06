class SimpleList:
    def __init__(self,items):
        self.items = list(items)

    def add(self,item):
        self.items.append(item)

    def __getitem__(self, index):
        return self.items[index]

    def sort(self):
        self.items.sort()

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return "SimpleList({})".format(self.items)


class SortedList(SimpleList):
    def __init__(self,items=()):
        super().__init__(items)
        self.sort()

    def add(self,item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({})".format(list(self))