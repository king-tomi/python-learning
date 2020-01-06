class Empty(Exception):
    pass


class ArrayStack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self,e):
        self.data.append(e)

    def top(self,):
        if self.is_empty():
            raise Empty("can't have an empty list")
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("empty stack")
        return self.data.pop()