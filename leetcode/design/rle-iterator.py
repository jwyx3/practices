# https://leetcode.com/problems/rle-iterator/
# Time: O(N)
# Space: O(N)

class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.i = 0
        

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        N = len(self.A)
        res = -1
        while self.i < N:
            if n > self.A[self.i]:
                n -= self.A[self.i]                
                self.i += 2
            else:
                self.A[self.i] -= n
                res = self.A[self.i + 1]
                break
        return res


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
