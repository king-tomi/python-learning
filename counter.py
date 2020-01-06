"""A program that models a hand-held counter"""
class Counter:

    def __init__(self):
        self._counter = 0

    def push(self):
        self._counter += 1
        return self._counter

    def reset(self):
        self._counter = 0