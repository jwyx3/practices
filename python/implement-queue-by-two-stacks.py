class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, element):
        self.stack1.append(element)

    def top(self):
        if self.stack2:
            return self.stack2[-1]
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def pop(self):
        self.top()
        return self.stack2.pop()

