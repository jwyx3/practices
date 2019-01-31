# https://leetcode.com/problems/remove-boxes/
# https://leetcode.com/problems/remove-boxes/discuss/101310/Java-top-down-and-bottom-up-DP-solutions
# more practice!!
# the idea to include k as part of state
# Time: O(n**4)
# Space: O(n**3)

class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        # dp(i, j, k): max points for A[i:j+1] with k A[i] within A[:i]
        # dp(i, j, k) = max(dp(i+1, m-1, 0) + dp(m, j, k + 1)), A[m] == A[i], i < m <= j
        # initial: dp(i, i-1, k) = 0, dp(i, i, k) = (k + 1) * (k + 1)
        # answer: dp(i, n-1, 0)
        
        n = len(boxes)
        memo = {}
        
        def dp(i, j, k):
            if i > j:
                return 0
            if (i, j, k) in memo:
                return memo[i, j, k]
            # reduce calculation
            while i < j and boxes[i] == boxes[i+1]:
                k += 1
                i += 1
            best = (k + 1) ** 2 + dp(i+1, j, 0)
            
            for m in xrange(i+1, j+1):
                if boxes[m] == boxes[i]:
                    best = max(best, dp(i+1, m-1, 0) + dp(m, j, k+1))
            memo[i, j, k] = best
            return best
        
        return dp(0, n-1, 0)
