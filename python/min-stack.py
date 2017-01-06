import sys


class MinStack(object):

    def __init__(self):
        self.nums = []

    def push(self, number):
        self.nums.append((number, min(
            number, self.nums[-1][1] if len(self.nums) > 0 else sys.maxint)))

    def pop(self):
        if len(self.nums) > 0:
            return self.nums.pop()[0]
        raise IndexError("pop from empty stack")

    def min(self):
        return self.nums[-1][1]
