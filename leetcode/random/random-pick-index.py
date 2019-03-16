# https://leetcode.com/problems/random-pick-index/
# Time: pick O(1); init O(N)
# Space: O(N)

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.indices = collections.defaultdict(list)
        for i, x in enumerate(nums):
            self.indices[x].append(i)
    
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        idx = self.indices[target]
        return idx[0] if len(idx) == 1 else random.choice(idx)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# use reservior sampling for all same elements
# Time: init O(1), pick O(N)
# Space: O(N), nums array

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
    
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        # k/k+j, j=[0, n-k)
        k, j, ans = 1, 0, -1  # -1 < all indices
        for i, x in enumerate(self.nums):
            if x != target:
                continue
            if random.randint(0, j) < k:
                ans = i
            j += 1
        return ans

