# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/solution/
# Say count(B) is the number of subarrays that have all elements less than or equal to B. From the above reasoning, the answer is count(R) - count(L-1).
# Time: O(N)
# Space: O(1)

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        def count(x):
            res = cur = 0
            for a in A:
                cur = cur + 1 if a <= x else 0
                res += cur
            return res
        
        return count(R) - count(L - 1)


