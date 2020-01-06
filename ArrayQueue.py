"""A Queue implementation.

   input: an array that is transformed into a queue

   output: a queue with all the basic methods defined with it."""
class Empty(Exception):
    pass


class ArrayQueue:

    DEFAULT_CAPACITY = 10

    def __int__(self):

        self.data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise Empty("empty stack")
        return self.data[self.front]

    def de_queue(self):
        if self.is_empty():
            raise Empty("empty stack")
        answer = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return answer

    def enqueue(self,e):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1

    def resize(self,cap):
        old = self.data
        self.data = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self.front = 0