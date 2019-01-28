# https://leetcode.com/problems/maximum-frequency-stack/
# https://leetcode.com/problems/maximum-frequency-stack/solution/
# similar to LRU. can use stack because it only support push and pop
# Time: O(1), push and pop
# Space: O(N)

class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.stack = []  # use len of stack to get max_freq

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > len(self.stack):
            self.stack.append([])
        self.stack[f - 1].append(x)        
        
    def pop(self):
        """
        :rtype: int
        """
        x = self.stack[-1].pop()
        if not self.stack[-1]:
            self.stack.pop()
        self.freq[x] -= 1
        return x
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
