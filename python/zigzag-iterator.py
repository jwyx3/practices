class ZigzagIterator:

    # @param {int[]} v1 v2 two 1d vectors
    def __init__(self, v1, v2):
        # initialize your data structure here
        self.q = [v for v in [v1, v2] if v]

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
