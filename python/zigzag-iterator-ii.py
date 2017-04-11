class ZigzagIterator2:

    # @param {int[][]} a list of 1d vectors
    def __init__(self, vecs):
        # initialize your data structure here
        self.q = [v for v in vecs if v]

    def next(self):
        # Write your code here
        v = self.q.pop(0)
        ans = v.pop(0)
        if v:
            self.q.append(v)
        return ans

    def hasNext(self):
        # Write your code here
        return len(self.q) > 0


# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result
