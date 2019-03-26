# https://leetcode.com/problems/max-stack/
# https://leetcode.com/problems/max-stack/solution/
# Time: popMax: O(N), others O(1)
# Space: O(N)
# TODO: use tree!!

class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        m = max(x, self.stack[-1][1] if self.stack else x)
        self.stack.append((x, m))
        

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()[0]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def peekMax(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        

    def popMax(self):
        """
        :rtype: int
        """
        m = self.stack[-1][1]
        b = []
        while self.stack[-1][0] != m:
            b.append(self.stack.pop()[0])
        self.stack.pop()
        map(self.push, reversed(b))
        return m


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
