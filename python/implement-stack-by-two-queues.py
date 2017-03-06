from collections import deque


class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queues = [deque(), deque()]
        self.index = 0

    # @param x, an integer, push a new item into the stack
    # @return nothing
    def push(self, x):
        self.queues[self.index].append(x)

    # @return nothing, pop the top of the stack
    def pop(self):
        index, next_index = self.index, (self.index + 1) % 2
        while self.queues[index]:
            top = self.queues[index].popleft()
            if self.queues[index]:
                self.queues[next_index].append(top)
        self.index = next_index

    # @return an integer, return the top of the stack
    def top(self):
        ans = None
        index, next_index = self.index, (self.index + 1) % 2
        while self.queues[index]:
            ans = self.queues[index].popleft()
            self.queues[next_index].append(ans)
        self.index = next_index
        return ans

    # @return an boolean, check the stack is empty or not.
    def isEmpty(self):
        return len(self.queues[self.index]) == 0
