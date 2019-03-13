# https://leetcode.com/problems/reach-a-number/
# https://leetcode.com/problems/reach-a-number/discuss/112986/Concise-Python-with-explanation-and-example
# Time: O(sqrt(N))
# Space: O(1)

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        # 1 + 2 + ... + k = target + d, 0<=d<k
        # d must be even
        k = int(math.floor(math.sqrt(target)))
        s = (k + 1) * k / 2
        while s < target:
            k += 1
            s += k
        # 1. because d is odd.
        # if k is odd, then we need add k + 1 and k + 2
        # if k is even, then we need to add k + 1
        # 2. d is even, reverse sign of x < k. so steps is still k
        return k if (target - s) % 2 == 0 else k + 1 + k % 2
        
