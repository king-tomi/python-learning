class LinkedStack:

    class Node:

        __slots__ = "element", "_next"

        def __init__(self,element,_next):
            self.element = element
            self._next = _next

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self,e):
        self.head = self.Node(e,self.head)
        self.size += 1

    def top(self):
        if self.is_empty():
            raise ValueError("empty stack")
        return self.head.element

    def pop(self):
        if self.is_empty():
            raise ValueError("empty stack")
        answer = self.head.element
        self.head = self.head._next
        self.size -= 1
        return answer