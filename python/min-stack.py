class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, number):
        min_value = number
        if self.stack:
            min_value = min(self.stack[-1][1], min_value)
        self.stack.append((number, min_value))

    def pop(self):
        return self.stack.pop()[0]

    def min(self):
        return self.stack[-1][1]
