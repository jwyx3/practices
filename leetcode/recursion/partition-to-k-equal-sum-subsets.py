# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
#
# tips
# 1) de-dup
# 2) fail early

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        target, rem = divmod(sum(nums), k)
        if rem: return False
        
        nums.sort()
        if nums[-1] > target: return False
        
        def search(groups):
            if not nums: return True
            
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                # de-dup
                if not group: break
            nums.append(v)
            
            return False
        
        return search([0] * k)
