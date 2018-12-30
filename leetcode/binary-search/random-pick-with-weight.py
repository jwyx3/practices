import random
import time
    
# https://leetcode.com/problems/random-pick-with-weight/
    
    
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.psums = []
        for i in xrange(len(w)):
            self.psums.append(w[i])
            if i > 0:
                self.psums[i] += self.psums[i-1]
        random.seed(time.time())

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(0, self.psums[-1] - 1)
        start, end = 0, len(self.psums) - 1
        while start < end:
            mid = (start + end) / 2
            # find first `mid` which self.psums[mid - 1] <= target < self.psums[mid]
            if target < self.psums[mid]:
                end = mid
            else:
                start = mid + 1
        return start


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
